package View;

import java.util.List;

import Controller.Controller;
import Controller.interfaces.iGetController;
import Controller.interfaces.iGetView;
import Model.Domain.Student;

public class View implements iGetView {

    private iGetController contr;

    public void setController(iGetController contr)
    {
        this.contr = contr;
    }

    public void callModel()
    {
        contr.update();
    }

     public void printAllStudent(List<Student> students) {
        System.out.println("----------- Список студентов ----------");
        for (Student s : students) {
            System.out.println(s);
        }
    }
}
