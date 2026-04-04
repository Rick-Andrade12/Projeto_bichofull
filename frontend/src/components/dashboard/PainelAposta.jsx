import { formatarMoeda } from "../../utils/formatters";

function PainelAposta({
  valorAposta,
  setValorAposta,
  tipoAposta,
  setTipoAposta,
  milhar,
  setMilhar,
  bichoSelecionado,
  apostar,
  resultadoSorteio,
}) {
  return (
    <div className="side-panel">
      <div className="aposta-panel">
        <h3>Fazer Aposta</h3>

        <label>Valor da aposta</label>
        <input
          type="number"
          placeholder="Digite o valor"
          value={valorAposta}
          onChange={(e) => setValorAposta(e.target.value)}
          min="1"
        />

        <label>Tipo da aposta</label>
        <select
          value={tipoAposta}
          onChange={(e) => setTipoAposta(e.target.value)}
        >
          <option value="grupo">Grupo</option>
          <option value="milhar">Milhar</option>
        </select>

        {tipoAposta === "grupo" && (
          <div className="resumo-escolha">
            <p>Bicho selecionado</p>
            <strong>
              {bichoSelecionado
                ? `${bichoSelecionado.nome} - Grupo ${bichoSelecionado.grupo}`
                : "Nenhum bicho selecionado"}
            </strong>
          </div>
        )}

        {tipoAposta === "milhar" && (
          <>
            <label>Digite a milhar</label>
            <input
              type="text"
              placeholder="Ex: 1234"
              value={milhar}
              onChange={(e) =>
                setMilhar(e.target.value.replace(/\D/g, "").slice(0, 4))
              }
            />
          </>
        )}
      </div>

      <div className="resultado-panel">
        <button className="apostar-btn" onClick={apostar}>
          Apostar
        </button>

        {resultadoSorteio && (
          <div className="resultado-box-fixo">
            <h4>Resultado da Rodada {resultadoSorteio.rodada}</h4>

            <p
              className={
                resultadoSorteio.ganhou
                  ? "resultado-ganhou"
                  : "resultado-perdeu"
              }
            >
              {resultadoSorteio.ganhou ? "Você ganhou!" : "Você perdeu!"}
            </p>

            <p>
              <strong>Valor apostado:</strong> R$ {formatarMoeda(resultadoSorteio.valorAposta)}
            </p>

            {resultadoSorteio.tipoAposta === "grupo" && resultadoSorteio.bichoEscolhido && (
              <p>
                <strong>Bicho apostado:</strong>{" "}
                {resultadoSorteio.bichoEscolhido.nome} - Grupo {resultadoSorteio.bichoEscolhido.grupo}
              </p>
            )}

            {resultadoSorteio.tipoAposta === "milhar" && (
              <p>
                <strong>Milhar digitada:</strong> {resultadoSorteio.milharDigitada}
              </p>
            )}

            {resultadoSorteio.ganhou && (
              <>
                <p>
                  <strong>Posição premiada:</strong> {resultadoSorteio.posicaoPremiada}º
                </p>

                <p className="premio-ganho">
                  <strong>Prêmio ganho:</strong> R$ {formatarMoeda(resultadoSorteio.premio)}
                </p>
              </>
            )}

            <div className="lista-sorteios">
              <h5>5 sorteios da rodada</h5>

              {resultadoSorteio.sorteios?.map((item) => {
                const premiado = item.posicao === resultadoSorteio.posicaoPremiada;

                return (
                  <div
                    key={item.id}
                    className={`item-sorteio ${premiado ? "item-sorteio-premiado" : ""}`}
                  >
                    <p>
                      <strong>{item.posicao}º prêmio</strong>
                    </p>

                    <p>
                      <strong>Bicho:</strong>{" "}
                      {item.bichoCompleto
                        ? `${item.bichoCompleto.emoji} ${item.bichoCompleto.nome}`
                        : item.bicho}
                    </p>

                    <p>
                      <strong>Grupo:</strong> {item.grupoFormatado}
                    </p>

                    <p>
                      <strong>Milhar:</strong> {item.milharFormatada}
                    </p>
                  </div>
                );
              })}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default PainelAposta;