const tempSlider = document.getElementById("Temp_slider") as HTMLInputElement;
const humSlider = document.getElementById("Hum_slider") as HTMLInputElement;
const tempValue = document.getElementById("temp_value")!;
const humValue = document.getElementById("hum_value")!;

async function updateFromSensor() {
  try {
    const res = await fetch("http://localhost:5000/data");
    const data = await res.json();

    // Aggiorna valori numerici
    tempValue.textContent = data.temperature.toFixed(1);
    humValue.textContent = data.humidity.toFixed(1);

    // Aggiorna slider coerenti con i limiti impostati
    tempSlider.value = data.temperature;
    humSlider.value = data.humidity;
  } catch (err) {
    console.error("Errore durante la lettura del sensore:", err);
  }
}

// aggiorna ogni 2 secondi
setInterval(updateFromSensor, 2000);
