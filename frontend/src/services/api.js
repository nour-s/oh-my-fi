import axios from 'axios';

const API_URL = 'http://localhost:8000/api/v1';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

const apiService = {
  getExpenses: async () => {
    const response = await api.get('/expenses');
    return response.data;
  },

  createExpense: async (expenseData) => {
    const response = await api.post('/expenses', expenseData);
    return response.data;
  },

  updateExpense: async (expenseId, expenseData) => {
    const response = await api.put(`/expenses/${expenseId}`, expenseData);
    return response.data;
  },

  deleteExpense: async (expenseId) => {
    const response = await api.delete(`/expenses/${expenseId}`);
    return response.data;
  },

  getIncomes: async () => {
    const response = await api.get('/incomes');
    return response.data;
  },

  createIncome: async (incomeData) => {
    const response = await api.post('/incomes', incomeData);
    return response.data;
  },

  updateIncome: async (incomeId, incomeData) => {
    const response = await api.put(`/incomes/${incomeId}`, incomeData);
    return response.data;
  },

  deleteIncome: async (incomeId) => {
    const response = await api.delete(`/incomes/${incomeId}`);
    return response.data;
  },
};

export default apiService;
