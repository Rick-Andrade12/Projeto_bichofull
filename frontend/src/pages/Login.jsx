import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import "../styles/auth.css";
import { loginUsuario } from "../services/authService";

function Login() {
  const [email, setEmail] = useState("");
  const [senha, setSenha] = useState("");
  const navigate = useNavigate();

  async function logar(evento) {
    evento.preventDefault();

    try {
      const dados = { email, senha };
      const resposta = await loginUsuario(dados);

      localStorage.setItem("access_token", resposta.access_token);
      localStorage.setItem("refresh_token", resposta.refresh_token);
      localStorage.setItem("token_type", resposta.token_type);

      alert("Login realizado com sucesso!");
      setEmail("");
      setSenha("");
      navigate("/dashboard");
    } catch (error) {
      console.log(error.response?.data || error.message);
      alert("Erro ao fazer login");
    }
  }

  return (
    <div className="auth-container">
      <form className="auth-form" onSubmit={logar}>
        <h1 className="auth-title">Login</h1>

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
          Entrar
        </button>

        <p className="auth-text">
          Não possui conta? <Link to="/cadastro">Cadastre-se</Link>
        </p>
      </form>
    </div>
  );
}

export default Login;