# Automação com Selenium e Python

Este repositório contém um projeto de automação de testes para o site [Automation Testing Demo](http://demo.automationtesting.in/Register.html) utilizando Python e Selenium. A estrutura do projeto foi projetada para facilitar a automação em diferentes partes do site, seguindo práticas de programação orientada a objetos para reutilização de código.

## 📂 Estrutura do Projeto

O projeto está organizado da seguinte forma:

````
CHALLENGECYBERPYTHON/
├── config/
│ └── config.yaml
├── src/
│ ├── core/
│ │ ├── init.py
│ │ ├── action_helper.py
│ │ └── driver_factory.py
│ ├── pages/
│ │ ├── init.py
│ │ ├── date_picker_page.py
│ │ ├── frame_page.py
│ │ ├── register_page.py
│ │ └── slider_page.py
│ └── utils/
│ ├── init.py
│ └── config_loader.py
├── tests/
│ ├── init.py
│ └── test_runner.py
└── venv/

- `config/`: Contém arquivos de configuração como o caminho do driver do navegador.
- `src/`: O diretório principal que contém o código fonte.
  - `core/`: Módulos essenciais como base do projeto e auxiliares de ação.
  - `pages/`: Módulos que representam cada página do site com seus elementos e lógicas específicas.
  - `utils/`: Módulos de apoio, como carregamento de configurações.
- `tests/`: Contém os scripts de teste automatizados.
- `venv/`: Diretório do ambiente virtual Python (não deve ser incluído no repositório).
````

## ⚙️ Configuração

Antes de executar os testes, você precisa configurar o ambiente:

1. Clone o repositório para sua máquina local.
2. Se você não tem um ambiente virtual configurado, crie um usando `python -m venv venv` e ative-o com `source venv/bin/activate` no macOS/Linux ou `venv\Scripts\activate` no Windows.
3. Instale as dependências com `pip install -r requirements.txt` (você precisará criar este arquivo de requirements ou instalar manualmente as dependências listadas abaixo).
4. Atualize o arquivo `config.yaml` com o caminho correto para o ChromeDriver ou o driver do navegador de sua escolha.

## Dependências

Este projeto depende das seguintes bibliotecas Python:

- Selenium WebDriver: Para interação com navegadores web.
- PyYAML: Para ler arquivos de configuração em YAML.
- Pytest: Para executar os testes.

Você pode instalar todas as dependências necessárias com `pip install selenium pytest pyyaml`.

## Executando os Testes

Com o ambiente configurado, você pode executar os testes da seguinte maneira:

```bash
pytest tests/
```

Os testes automatizados incluem:

1. Preenchimento e envio do formulário de registro.
2. Escrita dentro de um frame.
3. Inserção de data de nascimento nos campos do DatePicker.
4. Movimentação do slider para 50%.