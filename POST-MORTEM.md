# Post-Mortem — Missão de Release

## Time
- Tech Lead: John Nicholson Mendes de Oliveira
- Dev A: Francisco Henrique Marcelino de Oliveira
- Dev B: Fabrício Pereira de Sousa
- QA/Release: Fabrício Pereira de Sousa

---

## O que funcionou bem
- Criação de branches separadas para o desenvolvimento de cada funcionalidade, mantendo o código organizado e isolado durante o processo;
- Integração das funcionalidades na branch develop por meio de Pull Requests, permitindo revisão do código antes do merge;
- Introdução e correção de bug proposital na main através de uma branch hotfix, simulando um fluxo real de correção em produção;
- Mesclage, correta do hotfix tanto para a main quanto para a develop, garantindo que a correção não se perdesse nas próximas releases.

## O que deu errado ou foi difícil
A maior dificuldade foi gerar o conflito entre as branches feature/dev-a e feature/dev-b. Inicialmente, as duas branches ficavam com o mesmo conteúdo no repositório remoto, o que impedia o conflito de aparecer durante o rebase. Após trocarmos as funcções entre os memebros da equipe, conseguimos deixar as features no repositório remoto com os seus conteúdos diferentes, assim reproduzindo o cenário corretamente. Além disso, tivemos dificuldades em identificar a sequência de comandos necessária para resolver o conflito e continuar o rebase.

## Onde usamos rebase (e por quê)
Usamos git rebase origin/develop nas branches feature antes de abrir os PRs. Isso mantém o histórico linear e facilita a revisão do Tech Lead no git log.

## Onde usamos merge (e por quê)
Usamos merge ao integrar feature → develop via PR, e ao propagar o hotfix para main e develop. O merge preserva o contexto de quando cada integração aconteceu.

## O que faríamos diferente
Escrever descrições mais detalhadas no corpo dos Pull Requests, explicando melhor o raciocínio por trás de cada mudança feita no código