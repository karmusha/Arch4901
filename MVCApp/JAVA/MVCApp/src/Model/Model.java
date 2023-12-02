package Model;

import java.util.List;

import Controller.interfaces.iGetModel;
import Model.Domain.Student;

public class Model implements iGetModel {
        private List<Student> students;

        public Model(List<Student> students) {
            this.students = students;
        }

        public List<Student> getAllStudents()
        {
            return students;
        }
}
