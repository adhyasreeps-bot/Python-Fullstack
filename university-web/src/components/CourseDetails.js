import {useParams} from 'react-router-dom';
function CourseDetails() {
  const {courseId} = useParams();
  return (
    <div>
      <h1>Course Details</h1>
      <p>Course ID: {courseId}</p>
    </div>
  );
}
export default CourseDetails;