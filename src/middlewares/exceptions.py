from fastapi import Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import ValidationError


# TODO check why this return a 200 code.
async def validation_request_exception_handler(request: Request, exc: ValidationError) -> JSONResponse | None:
    """Customized exception for any Pydantic validation errors."""
    errors = []

    for ex in exc.errors():
        err_data = {}

        message = ex.get("msg")
        field = ex.get("loc")[-1]
        err_type = ex.get("type")
        input_data = ex.get("input")

        print("A VER EL ERROR AQUI", ex)
        if err_type == "missing":
            message = "This field is required."
        if err_type == "value_error":
            message = ex.get("ctx", {}).get("reason", message)

        err_data["message"] = message
        err_data["field"] = field
        err_data["input"] = input_data
        errors.append(err_data)

        print("=====================================")

    return JSONResponse(
        content={
            "error": True,
            "message": "Requested data missing.",
            "status_code": status.HTTP_422_UNPROCESSABLE_ENTITY,
            "details": errors
        }
    )
