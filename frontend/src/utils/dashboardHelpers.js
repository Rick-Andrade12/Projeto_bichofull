import { bichos } from "../data/bichos";

export function obterGrupoPorMilhar(milhar) {
  const numero = String(milhar).padStart(4, "0");
  const dezena = Number(numero.slice(-2));
  const ajustada = dezena === 0 ? 100 : dezena;
  return Math.ceil(ajustada / 4);
}

export function buscarBichoPorGrupo(grupo) {
  const grupoFormatado = String(grupo).padStart(2, "0");
  return bichos.find((bicho) => bicho.grupo === grupoFormatado) || null;
}

export function transformarHistorico(apostas) {
  return [...apostas].reverse().map((item) => {
    const grupoRelacionado =
      item.tipo === "grupo"
        ? Number(item.numero)
        : obterGrupoPorMilhar(item.numero);

    const bicho = buscarBichoPorGrupo(grupoRelacionado);

    return {
      id: item.id,
      tipo: item.tipo,
      tipoLabel: item.tipo === "grupo" ? "Grupo" : "Milhar",
      numeroFormatado:
        item.tipo === "grupo"
          ? String(item.numero).padStart(2, "0")
          : String(item.numero).padStart(4, "0"),
      valor: item.valor,
      premio: item.premio,
      status: item.status,
      bicho: bicho?.nome || "Bicho não encontrado",
      icone: bicho?.emoji || "🎲",
    };
  });
}
