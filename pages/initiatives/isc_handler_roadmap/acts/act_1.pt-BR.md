---

layout: col-sidebar
title: "Ato I - Observando por trás da cortina"
author: "Raphael Moreira"
contributors: 
permalink: /initiatives/isc_handler_roadmap/acts
tags: ["cybersecurity", "protocol", "http", "network", "response header", "xss", "csrf", "clickjacking", hsts", "csp", "ssl"]

---

{% include writers.html %}

[🇺🇸](act_1.md) | 🇧🇷

# Ato I - Observando por trás da cortina
Sempre que um site é acessado, uma série de processos ocorre nos bastidores através do protocolo [🔍Http](https://pt.wikipedia.org/wiki/Hypertext_Transfer_Protocol). Essa dinâmica 
é facilmente visível por meio das ferramentas de desenvolvedor do seu navegador. Nele é possível monitorar todo o tráfego 
relacionado a um determinado site, incluindo características como [🔍Código de Estado (Status Code)](https://www.rfc-editor.org/rfc/rfc9110.html#name-status-codes) e [🔍muitos outros](https://developer.chrome.com/docs/devtools/network?hl=pt-br).

Cada entrada na lista de requisições representa uma interação única, sendo possível a um site ter dezenas delas para 
formação do conteúdo. Dentre as diversas informações fornecidas, vamos destacar aqui um dos [🔍Cabeçalhos Http](https://developer.mozilla.org/en-US/docs/Glossary/HTTP_header)
que diz muito sobre seu servidor: o **Cabeçalho de Resposta**.

>**Aviso legal:** o OWASP não endossa nenhum vendedor ou ferramenta ao mencioná-lo. Se ele é citado, é porque acreditamos
> que esteja disponível gratuitamente para uso em projetos de código aberto. Sinta-se livre para usar a ferramenta que
> mais se adequa à sua necessidade.

## Cabeçalho de Resposta
Trata-se de um conjunto de informações passadas entre cliente e servidor. Ainda que seja personalizável, há um 
[🔍padrão bem definido](https://developer.mozilla.org/en-US/docs/Glossary/Response_header) sobre sua estrutura, conteúdo e uso. Por conta dessa flexibilidade, é comumente manipulado por 
invasores, logo, é importante que os desenvolvedores se atentem a não confiar cegamente nesse conteúdo.

Para observá-los, usaremos o [🔍DevTools](https://developer.chrome.com/docs/devtools?hl=pt-br) do navegador [Brave](https://brave.com/pt-br/download/). Com o navegador aberto, 
ative a aba [🔍Rede (Network)](https://developer.chrome.com/docs/devtools/network?hl=pt-br) e mantenha-na assim enquanto visita um site, como `https://owasp.org/`. Ao [inspecionar um dos itens](https://developer.chrome.com/docs/devtools/network?hl=pt-br#details) 
que aparecem na lista de requisições, você terá acesso a aba **Cabeçalho (Headers)**, onde encontrará a seção 
**Cabeçalho de Resposta (Response Header)**.

A informação contida ali irá variar conforme a configuração do servidor, aplicação ou serviço acessado. Não há uma lista 
correta do que deve existir, ou sua composição, pois em linhas gerais, depende da necessidade de cada site, contudo, 
sabemos o que definitivamente <u>não deve existir</u>, quando falamos de cibersegurança.

Em sua lista de boas práticas, o [OWASP](https://owasp.org/) reúne uma série de recomendações, como [🔍conteúdo seguro sugerido](https://owasp.org/www-project-secure-headers/index.html) e 
[🔍o que evitar](https://owasp.org/www-project-secure-headers/index.html#prevent-information-disclosure-via-http-headers) no **Cabeçalho de Resposta**.

## Verificando se surtiu efeito
Existem ferramentas online que te auxiliam na identificação e conferência não só do **Cabeçalho de Resposta**, como outros
dados significativos:

- [Security Header](https://securityheaders.com/?q=https%3A%2F%2Fowasp.org%2F&followRedirects=on): além de uma nota, o site 
lhe dá uma breve descrição e importância sobre cada cabeçalho.
- [Protocol Guard](https://protocolguard.com/scan/owasp.org): além das orientações sobre cada cabeçalho, ele cita algumas falhas
relacionada a [🔍Cifras SSL/TLS](https://www.ssl.com/pt/artigo/o-que-%C3%A9-ssl-tls-an-in-depth-guide/).

Dentre os **Cabeçalhos de Resposta**, vale destacar aqui 2 deles: o [🔍Transporte Estrito de Segurança (HSTS)](https://www.ssl.com/pt/artigo/o-que-%C3%A9-http-transporte-estrito-seguran%C3%A7a-hsts/)
e o [🔍Políticas de Segurança de Conteúdo (CSP)](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/CSP).

Enquanto o HSTS visa proteger sites contra ataques de downgrade de protocolo e sequestro de cookies, forçando a 
interação somente via HTTPS seguras, o CSP busca fazer o mesmo com o conteúdo estático que seu servidor disponibiliza (javascript, por exemplo), 
mitigando ataques cruzados. Ambos os cabeçalhos possuem uma característica em comum: devem ser inseridos de forma controlada, 
aos poucos, observando-se o comportamento final, pois depende muito de como a aplicação e/ou site foi concebido.

Para apoiar essa análise, temos as seguintes ferramentas:

- [CSP Policy Evaluator](https://csper.io/evaluator): a partir de uma Url, esta ferramenta lhe aponta as falhas e dá detalhes
    de como resolvê-los adequadamente.
- [Google CSP Evaluator](https://csp-evaluator.withgoogle.com/): a partir de uma Url ou um conjunto de políticas CSP, esta ferramenta
 lhe dá orientações sobre cada regra.
- [Qualys SSLLabs](https://www.ssllabs.com/ssltest/analyze.html?d=owasp.org): analisa profundamente as configurações SSL, detalhando
  certificados e chaves, bem como a existência do cabeçalho HSTS.
- [HSTS Preload](https://hstspreload.org/): avalia se suas políticas HSTS são elegíveis para uso do atributo [preload](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Headers/Strict-Transport-Security#pr%C3%A9-carregamento_-_strict_transport_security),
um recurso que, embora não faça parte da especificação original, tem seu valor de segurança ao garantir que sua aplicação fará
parte das listas centralizadas como a [🔍lista Chromium](https://www.chromium.org/hsts/) ou [🔍lista Firefox](https://searchfox.org/comm-central/source/mozilla/security/manager/ssl/nsSTSPreloadList.inc).

## Por que isso é importante?
Configurar corretamente os **Cabeçalhos de Resposta** é crucial por várias razões:

- **Segurança**: a má configuração pode expor informações sensíveis sobre o servidor ou aplicação, 
facilitando ataques como a divulgação de informações confidenciais (disclosure) ou ataques de injeção.

- **Privacidade**: alguns cabeçalhos de resposta podem conter informações pessoais dos usuários, como cookies ou tokens 
de autenticação. Configurá-los ajuda corretamente a proteger a privacidade dos usuários, evitando vazamento de informações.

- **Prevenção de ataques**: cabeçalhos bem configurados podem ajudar a prevenir ataques como [🔍Cross-Site Scripting (XSS)](https://owasp.org/www-community/attacks/xss/), 
[🔍 Cross-Site Request Forgery (CSRF)](https://owasp.org/www-community/attacks/csrf) e [🔍Clickjacking](https://cheatsheetseries.owasp.org/cheatsheets/Clickjacking_Defense_Cheat_Sheet.html), fornecendo políticas de segurança apropriadas.

- **Melhoria no desempenho**: alguns cabeçalhos de resposta podem influenciar o cache do navegador, permitindo uma melhor 
desempenho do site ao reduzir o número de solicitações feitas ao servidor.

- **Compatibilidade**: configurar os cabeçalhos de resposta garante corretamente a compatibilidade com diferentes navegadores 
e dispositivos, proporcionando uma experiência consistente aos usuários.

## Resumo
A atenção aos **Cabeçalhos de Resposta** é um bom ponto de partida para assegurar proteção à sua aplicação ou site. Embora
sejam configurações simples - _e em alguns casos, triviais_ -, são cruciais para acrescentar uma camada adicional em seu ambiente. 
Vale lembrar que se for mal configurado, pode relevar características sigilosas do seu ambiente, que podem ser explorados 
pelos atacantes. 

Seguir as diretrizes do OWASP irá ajudá-lo na jornada de manter seus sistemas protegidos contra alguns vetores de ataque. 
A configuração adequada dos **Cabeçalhos de Resposta** também contribui para a privacidade dos usuários, melhora no desempenho 
e na compatibilidade do site.

---

| [⬆️Retornar ao índice](../index.pt-BR.md) | Ir para o Ato 2 (breve) |
|-------------------------------------------|-------------------------|
