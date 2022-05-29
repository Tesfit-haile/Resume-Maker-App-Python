import flask
from CV_PROJECT import app, db,  forms, models



"""
    ==>>> gets all the posts form the cv.db
          send it to the home.jin 
          then the home.jin file loop through them and send them to the home page.
"""


# if u want the user_obj to be dynamic you can create a authentication and use user_obj = current_user
# i mean login form
@app.route('/')
def home():
    user_obj = models.User.query.filter_by(username="Tesfalem haile").first()
    all_projects = models.Project.query.all()
    all_experience=models.WorkExperience.query.all()

    all_education = models.Education.query.all()
    all_skills    = models.Skill.query.all()
    all_languages = models.Language.query.all()
    return flask.render_template('home.jin',
                                 user_obj=user_obj,
                                 all_projects=all_projects,
                                 all_experience=all_experience,
                                 all_education=all_education,
                                 all_skills=all_skills,
                                 all_languages=all_languages
                                 )






@app.route('/cvform', methods=['GET', 'POST'])
def cvform():
    user_obj = models.User.query.get(1)
    userCvForms   = forms.UserCvForm()
    workForm      = forms.WorkExperience()
    projectForm       = forms.Project()
    skillForm         = forms.Skill()
    educationForm     = forms.Education()
    languageForm      = forms.Language()
    if flask.request.method == 'GET':
        return flask.render_template('cvform.jin',
                                     userCvForms=userCvForms,
                                     workForm=workForm,
                                     projectForm=projectForm,
                                     skillForm=skillForm,
                                     educationForm=educationForm,
                                     languageForm=languageForm
                                     )

    # else:
    #     if userCvForms.validate_on_submit():
    #         user_obj = models.User()
    #
    #         user_obj.username = userCvForms.username.data
    #         user_obj.fathername = userCvForms.fathername.data
    #         user_obj.email      = userCvForms.email.data
    #         user_obj.age        = userCvForms.age.data
    #         user_obj.city       = userCvForms.city.data
    #         db.session.add(user_obj)
    #         db.session.commit()
    #         print('Correct user added')
    #         return flask.redirect(flask.url_for('cvform'))
    #
    #     if workForm.validate_on_submit():
    #         worke_obj = models.WorkExperience()
    #
    #         worke_obj.title       = workForm.title.data
    #         worke_obj.work        = workForm.work.data
    #         worke_obj.entery_date = workForm.entery_date.data
    #         worke_obj.exit_date   = workForm.exit_date.data
    #         worke_obj.experience_description = workForm.experience_description.data
    #         user_obj.user_experience.append(worke_obj)
    #
    #         db.session.add(worke_obj)
    #         db.session.commit()
    #         print('Correct work added')
    #         return flask.redirect(flask.url_for('cvform'))
    #
    #     if projectForm.validate_on_submit():
    #         project_obj = models.Project()
    #         project_obj.project = projectForm.project.data
    #         project_obj.project_description = projectForm.project_description.data
    #         user_obj.user_projects.append(project_obj)
    #         # project_obj.user_pro = project_obj
    #         db.session.add(project_obj)
    #         db.session.commit()
    #         print('Correct proj added')
    #         return flask.redirect(flask.url_for('cvform'))
    #
    #     if skillForm.validate_on_submit():
    #         skill_obj = models.Skill()
    #         skill_obj.skill = skillForm.skill.data
    #         skill_obj.skill_description = skillForm.skill_description.data
    #         db.session.add(skill_obj)
    #         db.session.commit()
    #         print('Correct skill added')
    #         return flask.redirect(flask.url_for('cvform'))
    #
    #     if educationForm.validate_on_submit():
    #         education_obj = models.Education()
    #
    #         education_obj.education = educationForm.education.data
    #         education_obj.university = educationForm.education.data
    #         education_obj.graduate_date = educationForm.graduate_date.data
    #         education_obj.education_description = educationForm.education_description.data
    #         db.session.add(education_obj)
    #         db.session.commit()
    #         print('Correct edu added ')
    #         return flask.redirect(flask.url_for('cvform'))
    #
    #     if languageForm.validate_on_submit():
    #         language_obj = models.Language()
    #         language_obj.language = languageForm.language.data
    #         db.session.add(language_obj)
    #         db.session.commit()
    #         print('Correct lang added')
    #         return flask.redirect(flask.url_for('cvform'))
    # return flask.render_template('cvform.jin', userCvForms=userCvForms)
    #




@app.route('/userAddress', methods=('GET', 'POST'))
def userAddress():
    userCvForms = forms.UserCvForm()
    if userCvForms.validate_on_submit():
        user_obj = models.User()
        user_obj.username = userCvForms.username.data
        user_obj.fathername = userCvForms.fathername.data
        user_obj.email = userCvForms.email.data
        user_obj.age = userCvForms.age.data
        user_obj.city = userCvForms.city.data
        # add here description [use it as a PROFILE]
        user_obj.description = userCvForms.description.data
        db.session.add(user_obj)
        db.session.commit()
        print('Correct user added')
        return flask.redirect(flask.url_for('workExperience'))
    return flask.render_template('userAddress.jin', userCvForms=userCvForms, )


@app.route('/workExperience', methods=('GET', 'POST'))
def workExperience():
    user_obj = models.User.query.get(1)
    workForm = forms.WorkExperience()
    if workForm.validate_on_submit():
        worke_obj = models.WorkExperience()
        worke_obj.title = workForm.title.data
        worke_obj.work = workForm.work.data
        worke_obj.entery_date = workForm.entery_date.data
        worke_obj.exit_date = workForm.exit_date.data
        worke_obj.experience_description = workForm.experience_description.data
        user_obj.user_experience.append(worke_obj)
        db.session.add(worke_obj)
        db.session.commit()
        print('Correct work added')
        return flask.redirect(flask.url_for('education'))
    return flask.render_template('workExper.jin', workForm=workForm)



@app.route('/education', methods=('GET', 'POST'))
def education():
    educationForm     = forms.Education()
    if educationForm.validate_on_submit():
        education_obj = models.Education()
        education_obj.education = educationForm.education.data
        education_obj.university = educationForm.education.data
        education_obj.graduate_date = educationForm.graduate_date.data
        education_obj.education_description = educationForm.education_description.data
        db.session.add(education_obj)
        db.session.commit()
        print('Correct edu added ')
        return flask.redirect(flask.url_for('project'))
    return flask.render_template('education.jin', educationForm=educationForm)




@app.route('/project', methods=('GET', 'POST'))
def project():
    user_obj = models.User.query.get(1)
    projectForm       = forms.Project()
    if projectForm.validate_on_submit():
        project_obj = models.Project()
        project_obj.project = projectForm.project.data
        project_obj.project_description = projectForm.project_description.data
        user_obj.user_projects.append(project_obj)
        # project_obj.user_pro = project_obj
        db.session.add(project_obj)
        db.session.commit()
        print('Correct proj added')
        return flask.redirect(flask.url_for('language'))
    return flask.render_template('project.jin', projectForm=projectForm)




@app.route('/language', methods=('GET', 'POST'))
def language():
    languageForm      = forms.Language()
    if languageForm.validate_on_submit():
        language_obj = models.Language()
        language_obj.language = languageForm.language.data
        db.session.add(language_obj)
        db.session.commit()
        print('Correct lang added')
        return flask.redirect(flask.url_for('skill'))
    return flask.render_template('language.jin', languageForm=languageForm)



@app.route('/skill', methods=('GET', 'POST'))
def skill():
    skillForm         = forms.Skill()
    if skillForm.validate_on_submit():
        skill_obj = models.Skill()
        skill_obj.skill = skillForm.skill.data
        skill_obj.skill_description = skillForm.skill_description.data
        db.session.add(skill_obj)
        db.session.commit()
        print('Correct skill added')
        return flask.redirect(flask.url_for('home'))
    return flask.render_template('skill.jin', skillForm=skillForm)



@app.route('/navbar', methods=('GET', 'POST'))
def navbar():
    return flask.render_template(navbar.jin)

