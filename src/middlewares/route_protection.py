from urllib.parse import urlparse

from fastapi import HTTPException, Request, status

from src.config.core import core_settings


#TODO improve func
async def origin_request(request: Request) -> None:
    """Check if referer or HOST request coming from FrontEnd app.
    :return: None."""
    origin = request.headers.get("origin")
    referer = request.headers.get("referer")

    print("========== ORIGIN DE LA PETICION =>", origin)
    print("========== REFERER DE LA PETICION =>", referer)

    if referer := request.headers.get("referer"):
        par = urlparse(referer)
        rf_orig = f"{par.scheme}://{par.netloc}"
        print("refer", referer)
        print("parsed", par)
        print("parsed origin", rf_orig)
        if referer not in core_settings.CORS_ORIGINS:
            print("No hay referer", referer)
            raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail={"message": "Route don't found."}
                )

    if origin := request.headers.get("origin"):
        if origin not in core_settings.CORS_ORIGINS:
            print("No hay origin", origin)
            raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail={"message": "Route don't found."}
                )

    if origin is None or referer is None:
        raise HTTPException(
                        status_code=status.HTTP_404_NOT_FOUND,
                        detail={"message": "Route don't found."}
                    )
