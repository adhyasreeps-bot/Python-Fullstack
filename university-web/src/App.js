// valid jsx
//function App() {
//  const universityName= "University Hub";
//
//  return (
//    <div className="main-container">
//      <h1>Welcome to {universityName}</h1>
//      <p>Manage your academic life.</p>
//    </div>
//  );
//}

//export default App;
import Navbar from './components/Navbar';
import Home from './components/Home';
import Contact from './components/Contact';
import About from './components/About';
import CourseDetails from './components/CourseDetails';
import StudentsPage from './components/StudentsPage';
import CoursesPage from './components/CoursesPage';
import Login from './components/Login';
import {Routes, Route , Link} from 'react-router-dom';
function App() {
  return (
    <div className="p-4">
      {/*Navigation
      <nav>
        <Link to="/">Home</Link>|
        <Link to="/students">Students</Link>|
        <Link to="/courses">Courses</Link>|
        <Link to="/about">About</Link>|
      </nav> */}
      <Navbar />
      <Routes>
        {/* login page */}
        <Route path="/login" element={<Login />} />
        {/* Home Page */}
        <Route path="/" element={<Home />} />
        {/* Contact Page */}
        <Route path="/contact" element={<Contact />} />
        {/* Students page */}
        <Route path="/students" element={<StudentsPage />} />  
        {/* Courses page */}
        <Route path="/courses" element={<CoursesPage />} />
        {/* Course Details Page */}
        <Route path="/courses/:courseId" element={<CourseDetails/>} />
        {/* About Page */}
        <Route path="/about" element={<About />} />
      </Routes>
    </div>
  );
}

export default App;

