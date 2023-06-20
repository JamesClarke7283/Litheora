import logging
from os import environ
from quart import Quart, render_template
from tortoise.contrib.quart import register_tortoise
from models import Site

logging.basicConfig(level=environ["LOG_LEVEL"])

app = Quart(__name__)

# Register Tortoise as a Quart extension
register_tortoise(
    app,
    db_url=environ["DATABASE_URL"],
    modules={"models": ["models"]},
    generate_schemas=True,
)


@app.route("/install")
async def install():
    return await render_template("install.html")

if __name__ == "__main__":
    app.run(port=8080)
