# Configuração do Curso

## Introdução

Nesta lição, veremos como executar os exemplos de código deste curso.

## Requisitos

- Uma conta no GitHub
- Python 3.12+

## Clonar ou Fazer Fork deste Repositório

Para começar, clone ou faça um fork do repositório no GitHub. Isso criará sua própria versão do material do curso, permitindo que você execute, teste e modifique o código!

Isso pode ser feito clicando no link para [fazer fork do repositório](https://github.com/microsoft/ai-agents-for-beginners/fork).

Agora você deve ter sua própria versão "forkada" deste curso, como mostrado abaixo:

![Repositório Forkado](../../../translated_images/forked-repo.eea246a73044cc984a1e462349e36e7336204f00785e3187b7399905feeada07.pt.png)

## Obtenha seu Token de Acesso Pessoal (PAT) do GitHub

Atualmente, este curso utiliza o Github Models Marketplace para oferecer acesso gratuito a Modelos de Linguagem de Grande Escala (LLMs) que serão usados para criar Agentes de IA.

Para acessar este serviço, você precisará criar um Token de Acesso Pessoal no GitHub.

Isso pode ser feito acessando as configurações de [Tokens de Acesso Pessoal](https://github.com/settings/personal-access-tokens) na sua conta do GitHub.

Selecione as opções `Fine-grained tokens` no lado esquerdo da sua tela.

Depois, selecione `Generate new token`.

![Gerar Token](../../../translated_images/generate-token.361ec40abe59b84ac68d63c23e2b6854d6fad82bd4e41feb98fc0e6f030e8ef7.pt.png)

Copie o novo token que você acabou de criar. Agora, adicione-o ao arquivo `.env` incluído neste curso.

## Adicione-o às Variáveis de Ambiente

Para criar seu arquivo `.env`, execute o comando abaixo no terminal:

```bash
cp .env.example .env
```

Isso copiará o arquivo de exemplo e criará um `.env` no seu diretório.

Abra o arquivo e cole o token que você criou no campo `GITHUB_TOKEN=` do arquivo .env.

## Instale os Pacotes Necessários

Para garantir que você tenha todos os pacotes Python necessários para executar o código, execute o comando abaixo no terminal.

Recomendamos criar um ambiente virtual Python para evitar conflitos e problemas.

```bash
pip install -r requirements.txt
```

Isso deve instalar os pacotes Python necessários.

Agora você está pronto para executar o código deste curso. Divirta-se aprendendo mais sobre o mundo dos Agentes de IA!

Se você tiver algum problema durante a configuração, participe do nosso [Discord da Comunidade Azure AI](https://discord.gg/kzRShWzttr) ou [crie um issue](https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst).
```

**Aviso Legal**:  
Este documento foi traduzido utilizando serviços de tradução baseados em IA. Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.