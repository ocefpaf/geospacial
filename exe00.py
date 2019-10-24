floripa = df.loc[df["municipio"] == "FLORIANÓPOLIS"]

mask = floripa.loc[
    floripa["municipio"] == "FLORIANÓPOLIS", "balneario_nome"
].str.lower().str.contains("sul")

floripa[mask]
