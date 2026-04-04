import BichoCard from "./BichoCard";

function BichoGrid({ bichos, bichoSelecionado, selecionarBicho }) {
  return (
    <div className="bichos-panel">
      <h3>Escolha seu Bicho</h3>

      <div className="bichos-grid">
        {bichos.map((bicho) => (
          <BichoCard
            key={bicho.nome}
            bicho={bicho}
            selecionado={bichoSelecionado?.nome === bicho.nome}
            onSelecionar={selecionarBicho}
          />
        ))}
      </div>
    </div>
  );
}

export default BichoGrid;
