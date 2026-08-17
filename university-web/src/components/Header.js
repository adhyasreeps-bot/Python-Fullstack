import React from 'react';

function Header() {
  return (
    <header className="app-header">
      <h1>University Hub Portal</h1>
      <nav>
        <a href="/">Home</a>{" "}
        <a href="/courses">courses</a>
      </nav>
    </header>
  );
}

export default Header;