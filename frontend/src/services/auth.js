import axios from 'axios';

const API_URL = 'http://localhost:8000/api/v1';

const authenticateUser = async () => {
  try {
    const response = await axios.get(`${API_URL}/auth/`);
    return response.data;
  } catch (error) {
    console.error('Error authenticating user:', error);
    throw error;
  }
};

export { authenticateUser };
