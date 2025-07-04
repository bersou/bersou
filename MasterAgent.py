!pip install langchain requests python-dotenv --quiet

import os
import requests
from langchain.llms.base import LLM
from typing import Optional, List

TOGETHER_API_KEY = "389e606346808577896b61b1aacf75d01295f375f4efe8c182b166e6e270e32e"

OPENWEATHER_API_KEY = "43947567d93c8fba85322709ac1bb2ca"

class TogetherLLM(LLM):
    model: str = "mistralai/Mixtral-8x7B-Instruct-v0.1"
    temperature: float = 0.7
    max_tokens: int = 1024

    @property
    def _llm_type(self) -> str:
        return "together"

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        headers = {
            "Authorization": f"Bearer {TOGETHER_API_KEY}",
            "Content-Type": "application/json"
        }

        json_data = {
            "model": self.model,
            "prompt": prompt,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "stop": stop or [],
        }

        response = requests.post("https://api.together.xyz/inference", headers=headers, json=json_data)

        try:
            resposta = response.json()
            return resposta["choices"][0]["text"]
        except KeyError:
            print("❌ Erro: a resposta não veio no formato esperado.")
            print("📩 Resposta da API:", resposta)
            raise
        except Exception as e:
            print("❌ Erro inesperado:", e)
            raise

llm = TogetherLLM()

def perguntar(pergunta: str):
    try:
        instrucoes = " Responda em português de forma clara e objetiva."
        prompt = pergunta.strip() + instrucoes
        resposta = llm(prompt)
        print("\U0001f9e0 Resposta:\n", resposta)
    except Exception as e:
        print("❌ Erro ao gerar resposta:", e)

def gerar_modelo_planilha(titulo: str = "Controle de Gastos"):
    prompt = f"""
Crie um modelo de planilha chamado '{titulo}' com colunas principais e exemplos de preenchimento. O objetivo é ajudar a organizar as informações de forma útil em uma planilha Excel. Dê exemplos de 5 linhas. Responda em português.
"""
    try:
        resposta = llm(prompt)
        print("\U0001f4ca Modelo de planilha:\n", resposta)
    except Exception as e:
        print("❌ Erro ao gerar modelo de planilha:", e)

!pip install langchain requests python-dotenv --quiet

import os
import requests
from langchain.llms.base import LLM
from typing import Optional, List

TOGETHER_API_KEY = "389e606346808577896b61b1aacf75d01295f375f4efe8c182b166e6e270e32e"

class TogetherLLM(LLM):
    model: str = "mistralai/Mixtral-8x7B-Instruct-v0.1"
    temperature: float = 0.7
    max_tokens: int = 1024

    @property
    def _llm_type(self) -> str:
        return "together"

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        headers = {
            "Authorization": f"Bearer {TOGETHER_API_KEY}",
            "Content-Type": "application/json"
        }

        json_data = {
            "model": self.model,
            "prompt": prompt,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "stop": stop or [],
        }

        response = requests.post("https://api.together.xyz/inference", headers=headers, json=json_data)

        try:
            resposta = response.json()
            return resposta["choices"][0]["text"]
        except KeyError:
            print("❌ Erro: a resposta não veio no formato esperado.")
            print("📩 Resposta da API:", resposta)
            raise
        except Exception as e:
            print("❌ Erro inesperado:", e)
            raise

llm = TogetherLLM()

def perguntar(pergunta: str):
    try:
        instrucoes = " Responda em português de forma clara e objetiva."
        prompt = pergunta.strip() + instrucoes
        resposta = llm(prompt)
        print("\U0001f9e0 Resposta:\n", resposta)
    except Exception as e:
        print("❌ Erro ao gerar resposta:", e)

def gerar_modelo_planilha(titulo: str = "Controle de Gastos"):
    prompt = f"""
Crie um modelo de planilha chamado '{titulo}' com colunas principais e exemplos de preenchimento. O objetivo é ajudar a organizar as informações de forma útil em uma planilha Excel. Dê exemplos de 5 linhas. Responda em português.
"""
    try:
        resposta = llm(prompt)
        print("\U0001f4ca Modelo de planilha:\n", resposta)
    except Exception as e:
        print("❌ Erro ao gerar modelo de planilha:", e)

!pip install langchain requests python-dotenv --quiet

import os
import requests
from langchain.llms.base import LLM
from typing import Optional, List

TOGETHER_API_KEY = "389e606346808577896b61b1aacf75d01295f375f4efe8c182b166e6e270e32e"

class TogetherLLM(LLM):
    model: str = "mistralai/Mixtral-8x7B-Instruct-v0.1"
    temperature: float = 0.7
    max_tokens: int = 1024

    @property
    def _llm_type(self) -> str:
        return "together"

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        headers = {
            "Authorization": f"Bearer {TOGETHER_API_KEY}",
            "Content-Type": "application/json"
        }

        json_data = {
            "model": self.model,
            "prompt": prompt,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "stop": stop or [],
        }

        response = requests.post("https://api.together.xyz/inference", headers=headers, json=json_data)

        try:
            resposta = response.json()
            return resposta["choices"][0]["text"]
        except KeyError:
            print("❌ Erro: a resposta não veio no formato esperado.")
            print("📩 Resposta da API:", resposta)
            raise
        except Exception as e:
            print("❌ Erro inesperado:", e)
            raise

llm = TogetherLLM()

def perguntar(pergunta: str):
    try:
        instrucoes = " Responda em português de forma clara e objetiva."
        prompt = pergunta.strip() + instrucoes
        resposta = llm(prompt)
        print("\U0001f9e0 Resposta:\n", resposta)
    except Exception as e:
        print("❌ Erro ao gerar resposta:", e)

def gerar_modelo_planilha(titulo: str = "Controle de Gastos"):
    prompt = f"""
Crie um modelo de planilha chamado '{titulo}' com colunas principais e exemplos de preenchimento. O objetivo é ajudar a organizar as informações de forma útil em uma planilha Excel. Dê exemplos de 5 linhas. Responda em português.
"""
    try:
        resposta = llm(prompt)
        print("\U0001f4ca Modelo de planilha:\n", resposta)
    except Exception as e:
        print("❌ Erro ao gerar modelo de planilha:", e)

print("✅ Tudo pronto! Use perguntar('Sua pergunta') ou gerar_modelo_planilha()")

TOGETHER_API_KEY = "389e606346808577896b61b1aacf75d01295f375f4efe8c182b166e6e270e32e"

class TogetherLLM(LLM):
    model: str = "mistralai/Mixtral-8x7B-Instruct-v0.1"
    temperature: float = 0.7
    max_tokens: int = 1024

    @property
    def _llm_type(self) -> str:
        return "together"

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        headers = {
            "Authorization": f"Bearer {TOGETHER_API_KEY}",
            "Content-Type": "application/json"
        }

        json_data = {
            "model": self.model,
            "prompt": prompt,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "stop": stop or [],
        }

        response = requests.post("https://api.together.xyz/inference", headers=headers, json=json_data)

        try:
            resposta = response.json()
            return resposta["choices"][0]["text"]
        except KeyError:
            print("❌ Erro: a resposta não veio no formato esperado.")
            print("📩 Resposta da API:", resposta)
            raise
        except Exception as e:
            print("❌ Erro inesperado:", e)
            raise

llm = TogetherLLM()

def perguntar(pergunta: str):
    try:
        instrucoes = " Responda em português de forma clara e objetiva."
        prompt = pergunta.strip() + instrucoes
        resposta = llm(prompt)
        print("\U0001f9e0 Resposta:\n", resposta)
    except Exception as e:
        print("❌ Erro ao gerar resposta:", e)

def gerar_modelo_planilha(titulo: str = "Controle de Gastos"):
    prompt = f"""
Crie um modelo de planilha chamado '{titulo}' com colunas principais e exemplos de preenchimento. O objetivo é ajudar a organizar as informações de forma útil em uma planilha Excel. Dê exemplos de 5 linhas. Responda em português.
"""
    try:
        resposta = llm(prompt)
        print("\U0001f4ca Modelo de planilha:\n", resposta)
    except Exception as e:
        print("❌ Erro ao gerar modelo de planilha:", e)

!pip install langchain requests python-dotenv --quiet

import os
import requests
from langchain.llms.base import LLM
from typing import Optional, List

%env TOGETHER_API_KEY=389e606346808577896b61b1aacf75d01295f375f4efe8c182b166e6e270e32e

class TogetherLLM(LLM):
    model: str = "mistralai/Mixtral-8x7B-Instruct-v0.1"
    temperature: float = 0.7
    max_tokens: int = 1024

    @property
    def _llm_type(self) -> str:
        return "together"

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        headers = {
            "Authorization": f"Bearer {os.getenv('TOGETHER_API_KEY')}",
            "Content-Type": "application/json"
        }

        json_data = {
            "model": self.model,
            "prompt": prompt,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "stop": stop or [],
        }

        response = requests.post("https://api.together.xyz/inference", headers=headers, json=json_data)

        try:
            resposta = response.json()
            return resposta["choices"][0]["text"]
        except KeyError:
            print("❌ Erro: a resposta não veio no formato esperado.")
            print("📩 Resposta da API:", resposta)
            raise
        except Exception as e:
            print("❌ Erro inesperado:", e)
            raise

llm = TogetherLLM()

def perguntar(pergunta: str):
    try:
        instrucoes = " Responda em português de forma clara e objetiva."
        prompt = pergunta.strip() + instrucoes
        resposta = llm(prompt)
        print("\U0001f9e0 Resposta:\n", resposta)
    except Exception as e:
        print("❌ Erro ao gerar resposta:", e)

def gerar_modelo_planilha(titulo: str = "Controle de Gastos"):
    prompt = f"""
Crie um modelo de planilha chamado '{titulo}' com colunas principais e exemplos de preenchimento. O objetivo é ajudar a organizar as informações de forma útil em uma planilha Excel. Dê exemplos de 5 linhas. Responda em português.
"""
    try:
        resposta = llm(prompt)
        print("\U0001f4ca Modelo de planilha:\n", resposta)
    except Exception as e:
        print("❌ Erro ao gerar modelo de planilha:", e)

print("✅ Tudo pronto! Use perguntar('Sua pergunta') ou gerar_modelo_planilha()")

@property
def _llm_type(self) -> str:
    return "together"

def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }

    json_data = {
        "model": self.model,
        "prompt": prompt,
        "temperature": self.temperature,
        "max_tokens": self.max_tokens,
        "stop": stop or [],
    }

    response = requests.post("https://api.together.xyz/inference", headers=headers, json=json_data)

    try:
        resposta = response.json()
        return resposta["choices"][0]["text"]
    except KeyError:
        print("❌ Erro: a resposta não veio no formato esperado.")
        print("📩 Resposta da API:", resposta)
        raise
    except Exception as e:
        print("❌ Erro inesperado:", e)
!pip install langchain requests python-dotenv --quiet

import os
import requests
from langchain.llms.base import LLM
from typing import Optional, List

%env TOGETHER_API_KEY=389e606346808577896b61b1aacf75d01295f375f4efe8c182b166e6e270e32e

class TogetherLLM(LLM):
    model: str = "mistralai/Mixtral-8x7B-Instruct-v0.1"
    temperature: float = 0.7
    max_tokens: int = 1024

    @property
    def _llm_type(self) -> str:
        return "together"

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        headers = {
            "Authorization": f"Bearer {os.getenv('TOGETHER_API_KEY')}",
            "Content-Type": "application/json"
        }

        json_data = {
            "model": self.model,
            "prompt": prompt,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "stop": stop or [],
        }

        response = requests.post("https://api.together.xyz/inference", headers=headers, json=json_data)

        try:
            resposta = response.json()
            return resposta["choices"][0]["text"]
        except KeyError:
            print("❌ Erro: a resposta não veio no formato esperado.")
            print("📩 Resposta da API:", resposta)
            raise
        except Exception as e:
            print("❌ Erro inesperado:", e)
            raise

# Cria o agente com o modelo da Together
llm = TogetherLLM()

# Função segura para fazer perguntas
def perguntar(pergunta: str):
    try:
        instrucoes = " Responda em português de forma clara e objetiva."
        prompt = pergunta.strip() + instrucoes
        resposta = llm(prompt)
        print("\U0001f9e0 Resposta:\n", resposta)
    except Exception as e:
        print("❌ Erro ao gerar resposta:", e)

# Função especial para gerar modelo de planilha
def gerar_modelo_planilha(titulo: str = "Controle de Gastos"):
    prompt = f"""
Crie um modelo de planilha chamado '{titulo}' com colunas principais e exemplos de preenchimento. O objetivo é ajudar a organizar as informações de forma útil em uma planilha Excel. Dê exemplos de 5 linhas. Responda em português.
"""
    try:
        resposta = llm(prompt)
        print("\U0001f4ca Modelo de planilha:\n", resposta)
    except Exception as e:
        print("❌ Erro ao gerar modelo de planilha:", e)

# Mensagem inicial
!pip install langchain requests python-dotenv --quiet

import os
import requests
from langchain.llms.base import LLM
from typing import Optional, List

%env TOGETHER_API_KEY=389e606346808577896b61b1aacf75d01295f375f4efe8c182b166e6e270e32e

class TogetherLLM(LLM):
    model: str = "mistralai/Mixtral-8x7B-Instruct-v0.1"
    temperature: float = 0.7
    max_tokens: int = 1024

    @property
    def _llm_type(self) -> str:
        return "together"

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        headers = {
            "Authorization": f"Bearer {os.getenv('TOGETHER_API_KEY')}",
            "Content-Type": "application/json"
        }

        json_data = {
            "model": self.model,
            "prompt": prompt,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "stop": stop or [],
        }

        response = requests.post("https://api.together.xyz/inference", headers=headers, json=json_data)

        try:
            resposta = response.json()
            return resposta["choices"][0]["text"]
        except KeyError:
            print("❌ Erro: a resposta não veio no formato esperado.")
            print("📩 Resposta da API:", resposta)
            raise
        except Exception as e:
            print("❌ Erro inesperado:", e)
            raise

# Cria o agente com o modelo da Together
llm = TogetherLLM()

# Função segura para fazer perguntas
def perguntar(pergunta: str):
    try:
        instrucoes = " Responda em português de forma clara e objetiva."
        prompt = pergunta.strip() + instrucoes
        resposta = llm(prompt)
        print("\U0001f9e0 Resposta:\n", resposta)
    except Exception as e:
        print("❌ Erro ao gerar resposta:", e)

# Função especial para gerar modelo de planilha
def gerar_modelo_planilha(titulo: str = "Controle de Gastos"):
    prompt = f"""
Crie um modelo de planilha chamado '{titulo}' com colunas principais e exemplos de preenchimento. O objetivo é ajudar a organizar as informações de forma útil em uma planilha Excel. Dê exemplos de 5 linhas. Responda em português.
"""
    try:
        resposta = llm(prompt)
        print("\U0001f4ca Modelo de planilha:\n", resposta)
    except Exception as e:
        print("❌ Erro ao gerar modelo de planilha:", e)

# Mensagem inicial
!pip install langchain requests python-dotenv --quiet

import os
import requests
from langchain.llms.base import LLM
from typing import Optional, List

%env TOGETHER_API_KEY=389e606346808577896b61b1aacf75d01295f375f4efe8c182b166e6e270e32e

class TogetherLLM(LLM):
    model: str = "mistralai/Mixtral-8x7B-Instruct-v0.1"
    temperature: float = 0.7
    max_tokens: int = 1024

    @property
    def _llm_type(self) -> str:
        return "together"

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        headers = {
            "Authorization": f"Bearer {os.getenv('TOGETHER_API_KEY')}",
            "Content-Type": "application/json"
        }

        json_data = {
            "model": self.model,
            "prompt": prompt,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "stop": stop or [],
        }

        response = requests.post("https://api.together.xyz/inference", headers=headers, json=json_data)

        try:
            resposta = response.json()
            return resposta["choices"][0]["text"]
        except KeyError:
            print("❌ Erro: a resposta não veio no formato esperado.")
            print("📩 Resposta da API:", resposta)
            raise
        except Exception as e:
            print("❌ Erro inesperado:", e)
            raise

# Cria o agente com o modelo da Together
llm = TogetherLLM()

# Função segura para fazer perguntas
def perguntar(pergunta: str):
    try:
        instrucoes = " Responda em português de forma clara e objetiva."
        prompt = pergunta.strip() + instrucoes
        resposta = llm(prompt)
        print("\U0001f9e0 Resposta:\n", resposta)
    except Exception as e:
        print("❌ Erro ao gerar resposta:", e)

# Função especial para gerar modelo de planilha
def gerar_modelo_planilha(titulo: str = "Controle de Gastos"):
    prompt = f"""
Crie um modelo de planilha chamado '{titulo}' com colunas principais e exemplos de preenchimento. O objetivo é ajudar a organizar as informações de forma útil em uma planilha Excel. Dê exemplos de 5 linhas. Responda em português.
"""
    try:
        resposta = llm(prompt)
        print("\U0001f4ca Modelo de planilha:\n", resposta)
    except Exception as e:
        print("❌ Erro ao gerar modelo de planilha:", e)

# Mensagem inicial
!pip install langchain requests python-dotenv --quiet

import os
import requests
from langchain.llms.base import LLM
from typing import Optional, List

%env TOGETHER_API_KEY=389e606346808577896b61b1aacf75d01295f375f4efe8c182b166e6e270e32e

class TogetherLLM(LLM):
    model: str = "mistralai/Mixtral-8x7B-Instruct-v0.1"
    temperature: float = 0.7
    max_tokens: int = 1024

    @property
    def _llm_type(self) -> str:
        return "together"

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        headers = {
            "Authorization": f"Bearer {os.getenv('TOGETHER_API_KEY')}",
            "Content-Type": "application/json"
        }

        json_data = {
            "model": self.model,
            "prompt": prompt,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "stop": stop or [],
        }

        response = requests.post("https://api.together.xyz/inference", headers=headers, json=json_data)

        try:
            resposta = response.json()
            return resposta["choices"][0]["text"]
        except KeyError:
            print("❌ Erro: a resposta não veio no formato esperado.")
            print("📩 Resposta da API:", resposta)
       