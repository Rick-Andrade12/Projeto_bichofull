import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import "../styles/auth.css";
import { cadastrarUsuario } from "../services/authService";

function Cadastro() {
  const [nome, setNome] = useState("");
  const [email, setEmail] = useState("");
  const [senha, setSenha] = useState("");
  const navigate = useNavigate();

  async function cadastrar(evento) {
    evento.preventDefault();

    try {
      const dados = { nome, email, senha };
      await cadastrarUsuario(dados);

      alert("Cadastro realizado com sucesso!");
      setNome("");
      setEmail("");
      setSenha("");
      navigate("/login");
    } catch (error) {
      console.log(error.response?.data || error.message);
      alert("Erro ao cadastrar");
    }
  }

  return (
    <div className="auth-container">
      <form className="auth-form" onSubmit={cadastrar}>
        <h1 className="auth-title">Cadastro de Usuário</h1>

        <input
          className="auth-input"
          placeholder="Nome"
          name="nome"
          type="text"
          value={nome}
          onChange={(e) => setNome(e.target.value)}
        />

        <input
          className="auth-input"
          placeholder="Email"
          name="email"
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />

        <input
          className="auth-input"
          placeholder="Senha"
          name="senha"
          type="password"
          value={senha}
          onChange={(e) => setSenha(e.target.value)}
        />

        <button className="auth-button" type="submit">
          Cadastrar
        </button>

        <p className="auth-text">
          Já possui conta? <Link to="/login">Entrar</Link>
        </p>
      </form>
    </div>
  );
}

export default Cadastro;