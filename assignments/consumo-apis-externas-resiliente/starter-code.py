import json
import time
from typing import Any

import requests

MAX_TENTATIVAS = 4
TIMEOUT_SEGUNDOS = 5

URLS_APIS = {
    "moedas": "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=brl",
    "tempo": "https://api.open-meteo.com/v1/forecast?latitude=-23.55&longitude=-46.64&current=temperature_2m",
}


def request_com_retry(url: str, max_tentativas: int = MAX_TENTATIVAS) -> dict[str, Any]:
    """Executa request GET com retry e backoff exponencial para falhas temporarias."""
    for tentativa in range(1, max_tentativas + 1):
        try:
            response = requests.get(url, timeout=TIMEOUT_SEGUNDOS)
            if response.status_code >= 500:
                raise requests.HTTPError(f"Erro temporario do servidor: {response.status_code}")
            response.raise_for_status()
            return response.json()
        except (requests.Timeout, requests.ConnectionError, requests.HTTPError) as exc:
            if tentativa == max_tentativas:
                raise RuntimeError(f"Falha apos {max_tentativas} tentativas: {exc}") from exc

            backoff = 2 ** (tentativa - 1)
            print(f"Tentativa {tentativa} falhou ({exc}). Nova tentativa em {backoff}s...")
            time.sleep(backoff)



def normalizar_moedas(data: dict[str, Any]) -> list[dict[str, Any]]:
    # TODO: Converter resposta da API de moedas para uma lista padronizada.
    # Exemplo de item esperado: {"fonte": "moedas", "chave": "bitcoin", "valor": 123456.0}
    raise NotImplementedError("Implemente a normalizacao da API de moedas")



def normalizar_tempo(data: dict[str, Any]) -> list[dict[str, Any]]:
    # TODO: Converter resposta da API de tempo para uma lista padronizada.
    # Exemplo de item esperado: {"fonte": "tempo", "chave": "temperature_2m", "valor": 22.5}
    raise NotImplementedError("Implemente a normalizacao da API de tempo")



def gerar_relatorio(dados_combinados: list[dict[str, Any]], falhas: dict[str, str]) -> None:
    print("\n=== Relatorio de Coleta ===")
    print(f"Total de registros validos: {len(dados_combinados)}")
    print(f"Falhas por API: {len(falhas)}")

    for api, erro in falhas.items():
        print(f"- {api}: {erro}")

    with open("saida_apis.json", "w", encoding="utf-8") as f:
        json.dump(dados_combinados, f, ensure_ascii=False, indent=2)

    print("Arquivo 'saida_apis.json' salvo com sucesso.")



def main() -> None:
    dados_combinados: list[dict[str, Any]] = []
    falhas: dict[str, str] = {}

    for nome_api, url in URLS_APIS.items():
        try:
            payload = request_com_retry(url)
            if nome_api == "moedas":
                dados_combinados.extend(normalizar_moedas(payload))
            elif nome_api == "tempo":
                dados_combinados.extend(normalizar_tempo(payload))
        except Exception as exc:  # noqa: BLE001
            falhas[nome_api] = str(exc)

    gerar_relatorio(dados_combinados, falhas)


if __name__ == "__main__":
    main()
