import React, { useState } from 'react';

function RegistrationForm() {

  // 1. State is an object, not just a string
  const [formData, setFormData] = useState({
    firstName: "",
    lastName: "",
    email: "",
    role: "student"
  });

  // 2. The Universal Handler
  const handleChange = (e) => {

    const { name, value } = e.target;

    // Update ONLY the field that changed, keep the rest
    setFormData(prevState => ({
      ...prevState, // Spread operator copies existing fields
      [name]: value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault(); // Stop page reload
    console.log(formData);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        name="firstName"
        placeholder="First Name"
        value={formData.firstName}
        onChange={handleChange}
      />
      <input
        type="text"
        name="lastName"
        placeholder="Last Name"
        value={formData.lastName}
        onChange={handleChange}
      />
      <input
        type="email"
        name="email"
        placeholder="Email"
        value={formData.email}
        onChange={handleChange}
      />
      <select name="role" value={formData.role} onChange={handleChange}>
        <option value="student">Student</option>
        <option value="instructor">Instructor</option>
      </select>
      <button type="submit">Register</button>
    </form>
  );
}

export default RegistrationForm;