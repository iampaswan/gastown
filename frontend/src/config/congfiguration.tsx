import axios from "axios";

const api = axios.create({
   baseURL: "http://127.0.0.1:8000",
});

export const researchApi = async (query: string) => {
   const response = await api.post(`/research?query=${encodeURIComponent(query)}`);
   return response.data;
};

export default api;

