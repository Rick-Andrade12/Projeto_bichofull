import { formatarMoeda } from "../../utils/formatters";

function SaldoCard({ saldo, totalGanho, totalPerdido, lucroPrejuizo }) {
  return (
    <section className="saldo-card">
      <div>
        <p className="saldo-label">Saldo Atual</p>
        <h2>R$ {formatarMoeda(saldo)}</h2>
      </div>

      <div className="saldo-stats">
        <div>
          <span>Total Ganho</span>
          <strong>R$ {formatarMoeda(totalGanho)}</strong>
        </div>

        <div>
          <span>Total Perdido</span>
          <strong>R$ {formatarMoeda(totalPerdido)}</strong>
        </div>

        <div>
          <span>Lucro/Prejuízo</span>
          <strong>R$ {formatarMoeda(lucroPrejuizo)}</strong>
        </div>
      </div>
    </section>
  );
}

export default SaldoCard;
