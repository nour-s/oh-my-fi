import React, { useState } from 'react';
import axios from 'axios';

const IncomeForm = () => {
    const [source, setSource] = useState('');
    const [amount, setAmount] = useState(0);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('/api/v1/income', {
                source,
                amount
            });
            console.log(response.data);
            // Add any success handling logic here
        } catch (error) {
            console.error(error);
            // Add any error handling logic here
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                placeholder="Source"
                value={source}
                onChange={(e) => setSource(e.target.value)}
            />
            <input
                type="number"
                placeholder="Amount"
                value={amount}
                onChange={(e) => setAmount(parseFloat(e.target.value))}
            />
            <button type="submit">Add Income</button>
        </form>
    );
};

export default IncomeForm;
