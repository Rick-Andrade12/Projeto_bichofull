import { formatarMoeda } from "../../utils/formatters";

function HistoricoLista({ historico }) {
  return (
    <section className="historico-panel">
      <h3>Suas Apostas</h3>

      <div className="historico-lista">
        {historico.length === 0 && (
          <p className="historico-vazio">Nenhuma aposta encontrada.</p>
        )}

        {historico.map((item) => (
          <div key={item.id} className="historico-card">
            <div className="historico-esquerda">
              <div className="historico-icone">{item.icone}</div>

              <div className="historico-info">
                <h4>
                  {item.tipoLabel}: {item.numeroFormatado} <span>({item.bicho})</span>
                </h4>
              </div>
            </div>

            <div className="historico-direita">
              <div className="historico-valores">
                <div>
                  <span>Apostado</span>
                  <strong>R$ {formatarMoeda(item.valor)}</strong>
                </div>

                {item.status === "ganhou" && (
                  <div>
                    <span>Prêmio</span>
                    <strong className="valor-premio">
                      R$ {formatarMoeda(item.premio)}
                    </strong>
                  </div>
                )}
              </div>

              <span
                className={
                  item.status === "ganhou"
                    ? "historico-badge ganhou"
                    : "historico-badge perdeu"
                }
              >
                {item.status === "ganhou" ? "Ganhou" : "Perdeu"}
              </span>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}

export default HistoricoLista;
