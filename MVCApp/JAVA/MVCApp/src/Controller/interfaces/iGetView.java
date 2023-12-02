package Controller.interfaces;

import java.util.List;

import Model.Domain.Student;

public interface iGetView {
     public void printAllStudent(List<Student> students);
     public void setController(iGetController control);
     public void callModel();
}
