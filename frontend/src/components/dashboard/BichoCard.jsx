function BichoCard({ bicho, selecionado, onSelecionar }) {
  return (
    <button
      type="button"
      className={`bicho-card ${selecionado ? "selecionado" : ""}`}
      onClick={() => onSelecionar(bicho)}
    >
      <div className="bicho-emoji">{bicho.emoji}</div>
      <h4>{bicho.nome}</h4>
      <p>Grupo {bicho.grupo}</p>
      <span>{bicho.faixa}</span>
    </button>
  );
}

export default BichoCard;
