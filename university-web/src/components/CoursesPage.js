import CourseCard from './CourseCard';
import RegistrationForm from './RegistrationForm';
import CourseList from './CourseList';
import SearchBar from './SearchBar';

function CoursesPage() {
  return (
        <div>
            {/* CourseCard Demo */}
            <h2>Course List</h2>
            <CourseCard title="History of Westeros"
            code="HIS101"
            credits={3}
            />

            <CourseCard title="Marine Biology"
            code="BIO201"
            credits={4}
            />
            
            <CourseCard title="Law"
            code="LAW301"
            credits={5}
            />

            {/*Form Section(Section-3 Demo*/}
            <h2>Register for Courses</h2>
            <RegistrationForm />

            <h2>All courses(Dynamic List)</h2>
            <CourseList />

            {/* SearchBar */}
            <h2>Search Courses</h2>
            <SearchBar />  
        </div>
    );
}

export default CoursesPage;