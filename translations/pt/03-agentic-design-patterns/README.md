# Princípios de Design de Agentes de IA

## Introdução

Existem muitas maneiras de pensar na construção de Sistemas de Agentes de IA. Considerando que a ambiguidade é uma característica, e não um defeito, no design de IA Generativa, às vezes é difícil para os engenheiros saberem por onde começar. Criamos um conjunto de Princípios de Design centrados no ser humano para permitir que os desenvolvedores construam sistemas de agentes centrados no cliente, capazes de atender às suas necessidades de negócios. Esses princípios de design não são uma arquitetura prescritiva, mas sim um ponto de partida para equipes que estão definindo e desenvolvendo experiências com agentes.

Em geral, os agentes devem:

- Ampliar e escalar as capacidades humanas (brainstorming, resolução de problemas, automação, etc.)
- Preencher lacunas de conhecimento (me atualizar em áreas de conhecimento, tradução, etc.)
- Facilitar e apoiar a colaboração nas formas como preferimos trabalhar com outras pessoas
- Nos tornar melhores versões de nós mesmos (por exemplo, coach de vida/gestor de tarefas, ajudando-nos a aprender habilidades de regulação emocional e mindfulness, construindo resiliência, etc.)

## Esta Aula Abrangerá

- O que são os Princípios de Design de Agentes
- Quais são algumas diretrizes a seguir ao implementar esses princípios de design
- Alguns exemplos de uso dos princípios de design

## Objetivos de Aprendizado

Após completar esta aula, você será capaz de:

1. Explicar o que são os Princípios de Design de Agentes
2. Explicar as diretrizes para o uso dos Princípios de Design de Agentes
3. Entender como construir um agente utilizando os Princípios de Design de Agentes

## Os Princípios de Design de Agentes

![Princípios de Design de Agentes](../../../translated_images/translated_images/agentic-design-principles.9f32a64bb6e2aa5a1bdffb70111aa724058bc248b1a3dd3c6661344015604cff.pt.png?WT.mc_id=academic-105485-koreyst)

### Agente (Espaço)

Este é o ambiente no qual o agente opera. Esses princípios orientam como projetamos agentes para interagir nos mundos físico e digital.

- **Conectar, não substituir** – ajudar a conectar pessoas a outras pessoas, eventos e conhecimentos acionáveis para permitir colaboração e conexão.
  - Agentes ajudam a conectar eventos, conhecimentos e pessoas.
  - Agentes aproximam as pessoas. Eles não são projetados para substituir ou diminuir o papel das pessoas.
- **Facilmente acessível, mas ocasionalmente invisível** – o agente opera em grande parte em segundo plano e só nos alerta quando é relevante e apropriado.
  - O agente é facilmente descoberto e acessível para usuários autorizados em qualquer dispositivo ou plataforma.
  - O agente suporta entradas e saídas multimodais (som, voz, texto, etc.).
  - O agente pode alternar perfeitamente entre primeiro plano e segundo plano; entre proativo e reativo, dependendo da percepção das necessidades do usuário.
  - O agente pode operar de forma invisível, mas o caminho de seus processos em segundo plano e a colaboração com outros agentes são transparentes e controláveis pelo usuário.

### Agente (Tempo)

Este é o modo como o agente opera ao longo do tempo. Esses princípios orientam como projetamos agentes que interagem através do passado, presente e futuro.

- **Passado**: Refletindo sobre o histórico que inclui tanto estado quanto contexto.
  - O agente fornece resultados mais relevantes com base na análise de dados históricos mais ricos, indo além do evento, pessoas ou estados isolados.
  - O agente cria conexões a partir de eventos passados e reflete ativamente sobre a memória para lidar com situações atuais.
- **Agora**: Mais estímulos do que notificações.
  - O agente adota uma abordagem abrangente ao interagir com pessoas. Quando um evento ocorre, o agente vai além de uma notificação estática ou formalidade. Ele pode simplificar fluxos ou gerar dinamicamente dicas para direcionar a atenção do usuário no momento certo.
  - O agente entrega informações com base no ambiente contextual, mudanças sociais e culturais, e adaptadas à intenção do usuário.
  - A interação com o agente pode ser gradual, evoluindo/crescendo em complexidade para capacitar os usuários a longo prazo.
- **Futuro**: Adaptando-se e evoluindo.
  - O agente se adapta a vários dispositivos, plataformas e modalidades.
  - O agente se adapta ao comportamento do usuário, necessidades de acessibilidade e é totalmente personalizável.
  - O agente é moldado e evolui por meio da interação contínua com o usuário.

### Agente (Núcleo)

Esses são os elementos-chave no núcleo do design de um agente.

- **Aceitar incertezas, mas estabelecer confiança**.
  - Um certo nível de incerteza do agente é esperado. A incerteza é um elemento-chave no design de agentes.
  - Confiança e transparência são camadas fundamentais no design de agentes.
  - Os humanos têm controle sobre quando o agente está ativado/desativado, e o status do agente é claramente visível em todos os momentos.

## Diretrizes Para Implementar Esses Princípios

Ao usar os princípios de design acima, siga as seguintes diretrizes:

1. **Transparência**: Informe o usuário que a IA está envolvida, como ela funciona (incluindo ações passadas) e como fornecer feedback e modificar o sistema.
2. **Controle**: Permita que o usuário personalize, especifique preferências e personalize, tendo controle sobre o sistema e seus atributos (incluindo a capacidade de esquecer).
3. **Consistência**: Busque experiências consistentes e multimodais em dispositivos e pontos de contato. Use elementos familiares de UI/UX sempre que possível (por exemplo, ícone de microfone para interação por voz) e reduza a carga cognitiva do cliente tanto quanto possível (por exemplo, respostas concisas, recursos visuais e conteúdo "Saiba Mais").

## Como Projetar um Agente de Viagem Usando Esses Princípios e Diretrizes

Imagine que você está projetando um Agente de Viagem. Aqui está como você poderia pensar em usar os Princípios de Design e Diretrizes:

1. **Transparência** – Informe ao usuário que o Agente de Viagem é um Agente habilitado por IA. Forneça algumas instruções básicas sobre como começar (por exemplo, uma mensagem de "Olá", prompts de exemplo). Documente isso claramente na página do produto. Mostre a lista de prompts que o usuário fez no passado. Deixe claro como fornecer feedback (botões de curtir/descurtir, botão "Enviar Feedback", etc.). Articule claramente se o Agente tem restrições de uso ou tópicos.
2. **Controle** – Certifique-se de que esteja claro como o usuário pode modificar o Agente após sua criação, com coisas como o Prompt do Sistema. Permita que o usuário escolha o quão detalhado o Agente deve ser, seu estilo de escrita e quaisquer limitações sobre o que o Agente não deve abordar. Permita que o usuário visualize e exclua quaisquer arquivos ou dados associados, prompts e conversas anteriores.
3. **Consistência** – Certifique-se de que os ícones para Compartilhar Prompt, adicionar um arquivo ou foto e marcar alguém ou algo sejam padrões e reconhecíveis. Use o ícone de clipe de papel para indicar upload/compartilhamento de arquivos com o Agente, e um ícone de imagem para indicar upload de gráficos.

## Recursos Adicionais
- [Práticas para Governança de Sistemas de IA Agentes | OpenAI](https://openai.com)
- [O Projeto HAX Toolkit - Microsoft Research](https://microsoft.com)
- [Caixa de Ferramentas de IA Responsável](https://responsibleaitoolbox.ai)
```

**Aviso Legal**:  
Este documento foi traduzido utilizando serviços de tradução baseados em IA. Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução humana profissional. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.