from flask import Flask, jsonify
import serial, re, time

app = Flask(__name__)

def extract_data(output):
    data = re.findall(r'\d+\.\d+', output)[0]
    return float(data)

def read_sensor():
    ser = serial.Serial('/dev/tty.usbmodem1101', 9600, timeout=2)
    time.sleep(1)  # tempo per stabilire la connessione

    temp = pres = alt = humid = None
    while not all([temp, pres, alt, humid]):
        line = ser.readline().decode(errors='ignore')
        if "Temperature" in line:
            temp = extract_data(line)
        elif "Pressure" in line:
            pres = extract_data(line)
        elif "Altitude" in line:
            alt = extract_data(line)
        elif "Humidity" in line:
            humid = extract_data(line)

    ser.close()
    return {"temperature": temp, "pressure": pres, "altitude": alt, "humidity": humid}

@app.route("/data")
def get_data():
    data = read_sensor()
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
