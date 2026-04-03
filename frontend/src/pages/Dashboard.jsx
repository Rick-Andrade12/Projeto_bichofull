import { useCallback, useEffect, useMemo, useState } from "react";
import { useNavigate } from "react-router-dom";
import "../styles/dashboard.css";

import SaldoCard from "../components/dashboard/SaldoCard";
import BichoGrid from "../components/dashboard/BichoGrid";
import PainelAposta from "../components/dashboard/PainelAposta";
import HistoricoLista from "../components/dashboard/HistoricoLista";

import { bichos } from "../data/bichos";
import {
  buscarBichoPorGrupo,
  transformarHistorico,
} from "../utils/dashboardHelpers";
import { buscarUsuarioLogado } from "../services/authService";
import {
  buscarHistorico,
  buscarSaldo,
  realizarAposta,
} from "../services/dashboardService";

function Dashboard() {
  const navigate = useNavigate();

  const [abaAtiva, setAbaAtiva] = useState("jogar");
  const [valorAposta, setValorAposta] = useState("");
  const [tipoAposta, setTipoAposta] = useState("grupo");
  const [milhar, setMilhar] = useState("");
  const [bichoSelecionado, setBichoSelecionado] = useState(null);
  const [resultadoSorteio, setResultadoSorteio] = useState(null);
  const [historicoBruto, setHistoricoBruto] = useState([]);
  const [menuPerfilAberto, setMenuPerfilAberto] = useState(false);
  const [nomeUsuario, setNomeUsuario] = useState("");
  const [saldo, setSaldo] = useState(0);
  const [carregando, setCarregando] = useState(true);

  const historico = useMemo(
    () => transformarHistorico(historicoBruto),
    [historicoBruto],
  );

  const totalGanho = useMemo(() => {
    return historicoBruto
      .filter((item) => item.status === "ganhou")
      .reduce((acc, item) => acc + Number(item.premio || 0), 0);
  }, [historicoBruto]);

  const totalPerdido = useMemo(() => {
    return historicoBruto
      .filter((item) => item.status === "perdeu")
      .reduce((acc, item) => acc + Number(item.valor || 0), 0);
  }, [historicoBruto]);

  const lucroPrejuizo = totalGanho - totalPerdido;
  const inicialUsuario = nomeUsuario
    ? nomeUsuario.charAt(0).toUpperCase()
    : "U";

  const logout = useCallback(() => {
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");
    localStorage.removeItem("token_type");
    navigate("/login");
  }, [navigate]);

  function selecionarBicho(bicho) {
    setBichoSelecionado(bicho);
  }

  const carregarDados = useCallback(async () => {
    try {
      setCarregando(true);

      const [usuario, carteira, historicoResponse] = await Promise.all([
        buscarUsuarioLogado(),
        buscarSaldo(),
        buscarHistorico(),
      ]);

      setNomeUsuario(usuario.nome);
      setSaldo(carteira.saldo);
      setHistoricoBruto(historicoResponse);
    } catch (error) {
      console.log(error.response?.data || error.message);
      alert("Erro ao carregar dados do dashboard.");
      logout();
    } finally {
      setCarregando(false);
    }
  }, [logout]);

  useEffect(() => {
    carregarDados();
  }, [carregarDados]);

  async function apostar() {
    if (!valorAposta) {
      alert("Digite o valor da aposta.");
      return;
    }

    if (tipoAposta === "grupo" && !bichoSelecionado) {
      alert("Selecione um bicho.");
      return;
    }

    if (tipoAposta === "milhar" && milhar.length !== 4) {
      alert("Digite uma milhar com 4 números.");
      return;
    }

    try {
      const numeroApostado =
        tipoAposta === "grupo"
          ? String(bichoSelecionado.grupo)
          : String(milhar);

      const resposta = await realizarAposta({
        tipo: tipoAposta,
        numero: numeroApostado,
        valor: Number(valorAposta),
      });

      const sorteiosFormatados = (resposta.sorteios || []).map((item) => ({
        ...item,
        grupoFormatado: String(item.grupo).padStart(2, "0"),
        milharFormatada: String(item.milhar).padStart(4, "0"),
        bichoCompleto: buscarBichoPorGrupo(item.grupo),
      }));

      setResultadoSorteio({
        ganhou: resposta.status === "ganhou",
        tipoAposta,
        bichoEscolhido: bichoSelecionado,
        valorAposta,
        milharDigitada: milhar,
        premio: resposta.premio,
        status: resposta.status,
        rodada: resposta.rodada,
        posicaoPremiada: resposta.posicao_premiada,
        sorteios: sorteiosFormatados,
      });

      setSaldo(resposta.saldo_atual);

      const novoHistorico = await buscarHistorico();
      setHistoricoBruto(novoHistorico);

      setValorAposta("");
      setMilhar("");
    } catch (error) {
      console.log("ERRO COMPLETO:", error);
      console.log("ERRO RESPONSE:", error.response?.data);

      const detail = error.response?.data?.detail;

      if (typeof detail === "string") {
        alert(detail);
      } else if (Array.isArray(detail)) {
        alert(detail.map((item) => item.msg).join("\n"));
      } else {
        alert("Erro ao realizar aposta.");
      }
    }
  }

  if (carregando) {
    return <div className="dashboard-page">Carregando...</div>;
  }

  return (
    <div className="dashboard-page">
      <header className="dashboard-header">
        <SaldoCard
          saldo={saldo}
          totalGanho={totalGanho}
          totalPerdido={totalPerdido}
          lucroPrejuizo={lucroPrejuizo}
        />

        <div className="perfil-mini-area">
          <button
            type="button"
            className="perfil-mini-avatar"
            onClick={() => setMenuPerfilAberto(!menuPerfilAberto)}
          >
            {inicialUsuario}
          </button>

          {menuPerfilAberto && (
            <div className="menu-perfil-dropdown">
              <p className="menu-perfil-nome">{nomeUsuario}</p>
              <button className="menu-perfil-logout" onClick={logout}>
                Sair
              </button>
            </div>
          )}
        </div>
      </header>

      <section className="tabs-area">
        <button
          className={abaAtiva === "jogar" ? "tab-btn ativa" : "tab-btn"}
          onClick={() => setAbaAtiva("jogar")}
        >
          Jogar
        </button>

        <button
          className={abaAtiva === "historico" ? "tab-btn ativa" : "tab-btn"}
          onClick={() => setAbaAtiva("historico")}
        >
          Histórico
        </button>
      </section>

      {abaAtiva === "jogar" && (
        <section className="dashboard-content">
          <BichoGrid
            bichos={bichos}
            bichoSelecionado={bichoSelecionado}
            selecionarBicho={selecionarBicho}
          />

          <PainelAposta
            valorAposta={valorAposta}
            setValorAposta={setValorAposta}
            tipoAposta={tipoAposta}
            setTipoAposta={setTipoAposta}
            milhar={milhar}
            setMilhar={setMilhar}
            bichoSelecionado={bichoSelecionado}
            apostar={apostar}
            resultadoSorteio={resultadoSorteio}
          />
        </section>
      )}

      {abaAtiva === "historico" && <HistoricoLista historico={historico} />}
    </div>
  );
}

export default Dashboard;
