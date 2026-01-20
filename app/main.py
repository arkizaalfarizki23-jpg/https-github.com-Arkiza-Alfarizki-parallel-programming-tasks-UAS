from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import dask.dataframe as dd

app = FastAPI()
DATABASE_URL = "sqlite:///./data.db"

@app.get("/list", response_class=HTMLResponse)
def list_data():
    ddf = dd.read_sql_table(
        "sensor_log",
        DATABASE_URL,
        index_col="id",
        npartitions=2
    )

    df = ddf.compute()

    html = "<h2>Data Sensor Log</h2><table border='1'>"
    html += "<tr><th>Lokasi</th><th>Suhu</th><th>Kelembapan</th></tr>"

    for _, row in df.iterrows():
        html += f"<tr><td>{row.lokasi}</td><td>{row.suhu}</td><td>{row.kelembapan}</td></tr>"

    html += "</table>"
    return html

