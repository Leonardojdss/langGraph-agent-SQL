CREATE TABLE faturamento_vendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mes INT,
    ano INT,
    cliente VARCHAR(100),
    cidade VARCHAR(100),
    estado VARCHAR(2),
    valor_venda DECIMAL(10,2),
    produto VARCHAR(100)
);