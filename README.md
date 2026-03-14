# DataRep

Repositório destinado ao armazenamento e versionamento de arquivos relacionados a **dados e estrutura de banco de dados** do projeto.

Ele centraliza **scripts SQL e arquivos de modelagem de dados**, facilitando a organização, manutenção e evolução da base de dados ao longo do tempo.

---

# Estrutura do Repositório

```
DataRep
│
├── data-sql
│   ├── Kori_DataLoad.sql
│   ├── V1_Kori_Script.sql
│   ├── V2_Kori_Script.sql
│   ├── V3_Kori_Alter_Grades_Alter_Report_Card.sql
│   ├── V4_Kori_Update_Final_Situation.sql
│   ├── V5_Kori_Update_Professors_Password.sql
│   ├── V6_Kori_Alter_And_Insert_Professors.sql
│   ├── V6_Kori_Update_Grade_Rep_FK_Cascade.sql
│   ├── V7_Create_Calendar_Events.sql
│   ├── V8_Updating_Table_Calendar_Events.sql
│   ├── V9_Adding_ADMFK_Table_Calendar_Events.sql
│   └── V10_Droping_the_not_null_constraint_calendar_events.sql
│
└── data-modeling
    ├── Kori_LogicalV3.brM3
    └── Kori_conceptualV4.brM3
```

---

# Scripts SQL (`data-sql`)

Este diretório contém **scripts SQL responsáveis pela criação, alteração e manutenção do banco de dados**.

Esses scripts incluem:

* criação de tabelas
* alterações de estrutura
* inserção de dados
* atualização de constraints
* manutenção de relacionamentos
* evolução do banco de dados

## Versionamento dos Scripts

Os scripts seguem um padrão de versionamento (`V1`, `V2`, `V3`, etc.), permitindo acompanhar a evolução do banco de dados de forma organizada.

| Versão | Descrição                                                                |
| ------ | ------------------------------------------------------------------------ |
| V1     | Estrutura inicial do banco                                               |
| V2     | Atualizações e ajustes adicionais                                        |
| V3     | Alterações na estrutura de notas e boletim                               |
| V4     | Atualização da lógica de situação final                                  |
| V5     | Atualização de senha dos professores                                     |
| V6     | Alterações e inserções relacionadas aos professores e atualização de FK  |
| V7     | Criação da tabela `calendar_events`                                      |
| V8     | Atualizações na estrutura da tabela `calendar_events`                    |
| V9     | Adição da chave estrangeira de administrador na tabela `calendar_events` |
| V10    | Remoção da constraint `NOT NULL` da tabela `calendar_events`             |

---

# Modelagem de Dados (`data-modeling`)

Este diretório contém arquivos de **modelagem do banco de dados**, utilizados para projetar e visualizar a estrutura do sistema.

## Arquivos

**Kori_LogicalV3.brM3**
Modelo lógico do banco de dados, representando tabelas, atributos e relacionamentos.

**Kori_conceptualV4.brM3**
Modelo conceitual do banco de dados, apresentando as entidades e seus relacionamentos de forma mais abstrata.

Esses arquivos são utilizados em ferramentas de modelagem de banco para facilitar a visualização e manutenção da arquitetura do sistema.


