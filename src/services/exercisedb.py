import json
import os
import urllib.request
from typing import Any, Dict, List
from urllib.request import HTTPError, Request

from fastapi import status
from fastapi.exceptions import HTTPException


class ExerciseRapidApiService:
    """Exercisedb rapidapi Service."""

    def __init__(self):
        self._api_url = os.getenv("EXERCISEDB_HOST_KEY")
        self._api_key = os.getenv("EXERCISEDB_API_KEY")

    def get_exercise_list(self, limit: int = 10, offset: int = 10) -> List[Dict[str, Any]]:
        """Get exercises list from ExerciseDbAPI.
        :param limit: qty of exercise to retrieve.
        :param offset: qty of results to omite.
        :return: List response of exercise get."""
        try:
            req_header = {
                "x-rapidapi-host": self._api_url,
                "x-rapidapi-key": self._api_key
                }

            req = Request(
                url=f"https://{self._api_url}/exercises?limit={limit}&offset={offset}",
                headers=req_header
                )

            with urllib.request.urlopen(req) as request:
                raw_data = request.read().decode("UTF-8")
                response = json.loads(raw_data)

                return response

        except HTTPError as http_err:
            print("Error llamando a servicio ExercseApi")
            raise HTTPException(
                status_code=http_err.status,
                detail={"message": "An unexpected error has ocurred."}
            ) from http_err
