import typer
from carooline_tecrmi_seamless import __version__
from dotenv import load_dotenv, find_dotenv
from typing import Optional
from enum import Enum
from .webcat_service import generate_api_key, gen_deep_link

load_dotenv(find_dotenv(".tecrmi.env"))

app = typer.Typer()


class TecRMIModule(str, Enum):
    rmi = "rmi"
    parts = "parts"
    home = "home"


class VehicleType(str, Enum):
    cars = "cars"
    trucks = "trucks"


class Display(str, Enum):
    modules = "modules"
    components = "components"


@app.command()
def get_api_key(
    catalog: str = typer.Option("TecrmiCatalog", envvar="TECRMI_CATALOG"),
    username: str = typer.Option("TecrmiUsername", envvar="TECRMI_USERNAME"),
    password: str = typer.Option("TecrmiPassword", envvar="TECRMI_PASSWORD"),
    default_ttl: Optional[int] = typer.Option(
        31536000, envvar="TECRMI_DEFAULT_TTL", help="Living duration of the generated TecRMI API Key"
    ),
    wsdl: str = typer.Option(
        "https://webservice.tecalliance.services/webcat30/v1/services/WebCat30WS.soapEndpoint?wsdl",
        envvar="TECRMI_WEBCAT_WSDL",
    ),
):
    """
    Get Api Key
    """
    api_key = generate_api_key(
        catalog=catalog,
        username=username,
        password=password,
        default_ttl=default_ttl,
        wsdl=wsdl,
    )

    if api_key:
        apiKey = typer.style(api_key, fg=typer.colors.GREEN, bold=True)
        typer.echo("API Key: %s" % apiKey)
    else:
        message = typer.style(
            "Couldn't get ApiKey, check your credentials", fg=typer.colors.WHITE, bg=typer.colors.RED
        )
        typer.echo(message)


@app.command()
def get_link(
    catalog: str = typer.Option("TecrmiCatalog", envvar="TECRMI_CATALOG"),
    username: str = typer.Option("TecrmiUsername", envvar="TECRMI_USERNAME"),
    password: str = typer.Option("TecrmiPassword", envvar="TECRMI_PASSWORD"),
    default_ttl: Optional[int] = typer.Option(
        31536000, envvar="TECRMI_DEFAULT_TTL", help="Living duration of the generated TecRMI API Key"
    ),
    wsdl: str = typer.Option(
        "https://webservice.tecalliance.services/webcat30/v1/services/WebCat30WS.soapEndpoint?wsdl",
        envvar="TECRMI_WEBCAT_WSDL",
    ),
    lang: Optional[str] = typer.Option("fr", envvar="TECRMI_LANG"),
    url: Optional[str] = typer.Option("https://web.tecalliance.net", envvar="TECRMI_WEBCAT_URL"),
    module: TecRMIModule = TecRMIModule.rmi,
    vehicle_type: VehicleType = VehicleType.cars,
    type_id: Optional[str] = typer.Option(None, help="KType or NType (Without the 100 prefix)"),
    display: Display = Display.modules,
    siv: Optional[str] = typer.Option(None, help="SIV search is subject to the access rights of the credentials"),
    vin: Optional[str] = typer.Option(None, help="VIN search is subject to the access rights of the credentials"),
):
    """
    Get API Key and generate TecRMI seamless deeplink for given parameters.

    Example usage:
        carooline-tecrmi-seamless get-link --type-id=9465
    """
    api_key = generate_api_key(
        catalog=catalog,
        username=username,
        password=password,
        default_ttl=default_ttl,
        wsdl=wsdl,
    )

    if not api_key:
        message = typer.style(
            "Couldn't get ApiKey, check your credentials", fg=typer.colors.WHITE, bg=typer.colors.RED
        )
        typer.echo(message)
        return
    target_url = gen_deep_link(
        catalog=catalog,
        api_key=api_key,
        lang=lang,
        url=url,
        module=module,
        vehicle_type=vehicle_type,
        type_id=type_id,
        display=display,
        siv=siv,
        vin=vin,
    )
    target_url = typer.style(target_url, fg=typer.colors.GREEN, bold=True)
    typer.echo(target_url)


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return
