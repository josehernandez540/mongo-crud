const API = "https://mongo-crud-a5vs.onrender.com"

const form = document.getElementById("clienteForm")

form.addEventListener("submit", async (e) => {
    e.preventDefault()

    await crearCliente()
})

function showToast(message) {

    const toast = document.getElementById("toast")

    toast.innerText = message

    toast.classList.add("show")

    setTimeout(() => {
        toast.classList.remove("show")
    }, 3000)
}

async function crearCliente() {

    const body = {
        nombre: document.getElementById("nombre").value,
        telefono: document.getElementById("telefono").value,
        correo: document.getElementById("correo").value,
        direccion: document.getElementById("direccion").value
    }

    const response = await fetch(`${API}/clientes/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(body)
    })

    if (!response.ok) {
        showToast("Error al crear cliente")
        return
    }

    form.reset()

    showToast("Cliente registrado correctamente")

    listarClientes()
}

async function listarClientes() {

    const response = await fetch(`${API}/clientes/`)

    const clientes = await response.json()

    const container = document.getElementById("clientes")

    container.innerHTML = ""

    clientes.forEach(cliente => {

        container.innerHTML += `
            <div class="cliente-card">

                <div class="avatar">
                    <i class="fa-solid fa-user"></i>
                </div>

                <h3>${cliente.nombre}</h3>

                <div class="cliente-info">

                    <span>
                        <i class="fa-solid fa-phone"></i>
                        ${cliente.telefono}
                    </span>

                    <span>
                        <i class="fa-solid fa-envelope"></i>
                        ${cliente.correo}
                    </span>

                    <span>
                        <i class="fa-solid fa-location-dot"></i>
                        ${cliente.direccion}
                    </span>

                </div>

                <button
                    class="delete-btn"
                    onclick="eliminarCliente('${cliente._id}')"
                >
                    <i class="fa-solid fa-trash"></i>
                    Eliminar
                </button>

            </div>
        `
    })
}

async function eliminarCliente(id) {

    const confirmacion = confirm("¿Deseas eliminar este cliente?")

    if (!confirmacion) return

    await fetch(`${API}/clientes/${id}`, {
        method: "DELETE"
    })

    showToast("Cliente eliminado")

    listarClientes()
}

async function cargarReportes() {

    const total = await fetch(`${API}/reportes/total-envios`)
    const promedio = await fetch(`${API}/reportes/promedio-valor`)
    const max = await fetch(`${API}/reportes/max-valor`)
    const min = await fetch(`${API}/reportes/min-valor`)
    const estados = await fetch(`${API}/reportes/envios-por-estado`)

    const totalData = await total.json()
    const promedioData = await promedio.json()
    const maxData = await max.json()
    const minData = await min.json()
    const estadosData = await estados.json()

    document.getElementById("reportes").innerHTML = `

        <div class="report-card">
            <i class="fa-solid fa-sack-dollar"></i>
            <p>Total envíos</p>
            <h3>$${totalData.totalEnvios || 0}</h3>
        </div>

        <div class="report-card">
            <i class="fa-solid fa-chart-column"></i>
            <p>Promedio</p>
            <h3>$${Math.round(promedioData.promedioValor || 0)}</h3>
        </div>

        <div class="report-card">
            <i class="fa-solid fa-arrow-trend-up"></i>
            <p>Valor máximo</p>
            <h3>$${maxData.mayorValor || 0}</h3>
        </div>

        <div class="report-card">
            <i class="fa-solid fa-arrow-trend-down"></i>
            <p>Valor mínimo</p>
            <h3>$${minData.menorValor || 0}</h3>
        </div>

        <div class="report-card">
            <i class="fa-solid fa-boxes-stacked"></i>
            <p>Estados de envíos</p>

            <div class="estados-list">
                ${estadosData.map(e => `
                    <div class="estado-item">
                        <span>${e._id}</span>
                        <strong>${e.cantidad}</strong>
                    </div>
                `).join("")}
            </div>

        </div>
    `

    showToast("Reportes actualizados")
}

listarClientes()
cargarReportes()
