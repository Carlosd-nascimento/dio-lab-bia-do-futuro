# Passo a Passo de Execução
## Setup do Ollama
```bash
# 1- Instalar o Ollama(ollama.com)

# 2- Instalar o modelo
ollama pull gpt-oss:20b

# 3- Testar se está funcionando
ollama run gpt-oss:20b "Olá!"
```

# Código da Aplicação

Todo o código fonte está no arquivo `app.py`.

## Estrutura

```
src/
├── app.py              # Aplicação principal (Streamlit)
```

## Como Rodar

```bash
# Instalar dependências
pip install streamlit pandas requests

# Garantir que o Ollama está rodando
ollama serve

# Rodar a aplicação
python -m streamlit run .\src\app.py
```
# Evidências de Execução
<img width="1875" height="909" alt="image" src="https://github.com/user-attachments/assets/c0fe61fd-47e8-4d51-abb9-00acaf1eb42f" />

