import api from "./api";

export async function cadastrarUsuario(dados) {
  const response = await api.post("/auth/cadastrar", dados);
  return response.data;
}

export async function loginUsuario(dados) {
  const response = await api.post("/auth/login", dados);
  return response.data;
}

export async function buscarUsuarioLogado() {
  const response = await api.get("/auth/me");
  return response.data;
}