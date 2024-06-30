import React from 'react';

const Navbar = () => {
    return (
        <nav>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/expenses">Expenses</a></li>
                <li><a href="/income">Income</a></li>
                <li><a href="/analytics">Analytics</a></li>
            </ul>
        </nav>
    );
};

export default Navbar;
