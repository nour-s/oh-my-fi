import React, { useState, useEffect } from 'react';
import axios from '../services/api';
import { Link } from 'react-router-dom';

const Home = () => {
    const [userData, setUserData] = useState(null);

    useEffect(() => {
        const fetchUserData = async () => {
            try {
                const response = await axios.get('/user/data');
                setUserData(response.data);
            } catch (error) {
                console.error('Error fetching user data: ', error);
            }
        };

        fetchUserData();
    }, []);

    return (
        <div>
            <h1>Welcome to Your Personal Finance Dashboard</h1>
            {userData && (
                <div>
                    <p>Name: {userData.name}</p>
                    <p>Email: {userData.email}</p>
                    <p>Balance: ${userData.balance}</p>
                </div>
            )}
            <Link to="/expenses">View Expenses</Link>
            <Link to="/income">View Income</Link>
            <Link to="/analytics">View Analytics</Link>
        </div>
    );
};

export default Home;
