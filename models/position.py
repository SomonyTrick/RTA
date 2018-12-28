class Position:
    def __init__(self, projectname, company, post, persons, edu, degree, majors, target, status):
        self.projectname = projectname.strip()
        self.company = company.strip()
        self.post = post.replace('\t', '').replace('\n', '').replace(' ', '').strip()
        self.persons = persons.strip()
        self.edu = edu.strip()
        self.degree = degree.strip()
        self.majors = majors.replace('\t', '').replace('\n', '').replace(' ', '').strip()
        self.target = target.strip()
        self.status = status.strip()

        # 截取岗位
        self.post = self.post[0:self.post.index('[')]

    def show(self):
        return {
                'projectname': self.projectname,
                'company': self.company,
                'post': self.post,
                'persons': self.persons,
                'edu': self.edu,
                'degree': self.degree,
                'majors': self.majors,
                'target': self.target,
                'status': self.status
            }