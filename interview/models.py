from django.db import models
from django.contrib.auth.models import User

from jobs.models import DEGREE_TYPE

# 第一轮面试结果
FIRST_INTERVIEW_RESULT_TYPE = (
    ("2nd Round", "2nd Round"),
    ("Pending", "Pending"),
    ("Rejected", "Rejected"),
)

# 复试面试建议
INTERVIEW_RESULT_TYPE = (
    ("Accepted", "Accepted"),
    ("Pending", "Pending"),
    ("Rejected", "Rejected"),
)


# HR终面结论
HR_SCORE_TYPE = (("S", "S"), ("A", "A"), ("B", "B"), ("C", "C"))


class Candidate(models.Model):
    # 基础信息
    userid = models.IntegerField(
        unique=True, blank=True, null=True, verbose_name="Candidate ID"
    )
    username = models.CharField(max_length=135, verbose_name="Candidate Name")
    city = models.CharField(max_length=135, verbose_name="City")
    phone = models.CharField(max_length=135, verbose_name="Mobile")
    email = models.EmailField(max_length=135, blank=True, verbose_name="Email")
    apply_position = models.CharField(
        max_length=135, blank=True, verbose_name="Apply Position"
    )
    born_address = models.CharField(max_length=135, blank=True, verbose_name="Location")
    gender = models.CharField(max_length=135, blank=True, verbose_name="Gender")
    candidate_remark = models.CharField(
        max_length=135, blank=True, verbose_name="Additional Info"
    )

    # 学校与学历信息
    bachelor_school = models.CharField(
        max_length=135, blank=True, verbose_name="Bachelor"
    )
    master_school = models.CharField(max_length=135, blank=True, verbose_name="Master")
    doctor_school = models.CharField(max_length=135, blank=True, verbose_name="Doctor")
    major = models.CharField(max_length=135, blank=True, verbose_name="Major")
    degree = models.CharField(
        max_length=135, choices=DEGREE_TYPE, blank=True, verbose_name="Degree"
    )

    # 综合能力测评成绩，笔试测评成绩
    test_score_of_general_ability = models.DecimalField(
        decimal_places=1,
        null=True,
        max_digits=3,
        blank=True,
        verbose_name="Overall Score",
    )
    paper_score = models.DecimalField(
        decimal_places=1,
        null=True,
        max_digits=3,
        blank=True,
        verbose_name="Paper Score",
    )

    # 第一轮面试记录
    first_score = models.DecimalField(
        decimal_places=1,
        null=True,
        max_digits=2,
        blank=True,
        verbose_name="1st Round Score",
        help_text="1-5，Excellent: >=4.5，Good: 4-4.4，Fair: 3.5-3.9，Average: 3-3.4，Poor: <3",
    )
    first_learning_ability = models.DecimalField(
        decimal_places=1,
        null=True,
        max_digits=2,
        blank=True,
        verbose_name="Ability to Learn",
    )
    first_professional_competency = models.DecimalField(
        decimal_places=1,
        null=True,
        max_digits=2,
        blank=True,
        verbose_name="Professional Competence",
    )
    first_advantage = models.TextField(
        max_length=1024, blank=True, verbose_name="Advantages"
    )
    first_disadvantage = models.TextField(
        max_length=1024, blank=True, verbose_name="Concerns"
    )
    first_result = models.CharField(
        max_length=256,
        choices=FIRST_INTERVIEW_RESULT_TYPE,
        blank=True,
        verbose_name="First Round Results",
    )
    first_recommend_position = models.CharField(
        max_length=256, blank=True, verbose_name="Recommended Positions"
    )
    first_interviewer_user = models.ForeignKey(
        User,
        related_name="first_interviewer_user",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="Interviewer",
    )

    first_remark = models.CharField(
        max_length=135, blank=True, verbose_name="First Round Remarks"
    )

    # 第二轮面试记录
    second_score = models.DecimalField(
        decimal_places=1,
        null=True,
        max_digits=2,
        blank=True,
        verbose_name="2nd Round Score",
        help_text="1-5，Excellent: >=4.5，Good: 4-4.4，Fair: 3.5-3.9，Average: 3-3.4，Poor: <3",
    )
    second_learning_ability = models.DecimalField(
        decimal_places=1,
        null=True,
        max_digits=2,
        blank=True,
        verbose_name="Ability to Learn",
    )
    second_professional_competency = models.DecimalField(
        decimal_places=1,
        null=True,
        max_digits=2,
        blank=True,
        verbose_name="Professional Competence",
    )
    second_pursue_of_excellence = models.DecimalField(
        decimal_places=1,
        null=True,
        max_digits=2,
        blank=True,
        verbose_name="Pursuit of Excellence",
    )
    second_communication_ability = models.DecimalField(
        decimal_places=1,
        null=True,
        max_digits=2,
        blank=True,
        verbose_name="Communication",
    )
    second_pressure_score = models.DecimalField(
        decimal_places=1,
        null=True,
        max_digits=2,
        blank=True,
        verbose_name="Stress Management",
    )
    second_advantage = models.TextField(
        max_length=1024, blank=True, verbose_name="Advantages"
    )
    second_disadvantage = models.TextField(
        max_length=1024, blank=True, verbose_name="Concerns"
    )
    second_result = models.CharField(
        max_length=256,
        choices=INTERVIEW_RESULT_TYPE,
        blank=True,
        verbose_name="Second Round Results",
    )
    second_recommend_position = models.CharField(
        max_length=256, blank=True, verbose_name="Recommended Position"
    )
    second_interviewer_user = models.ForeignKey(
        User,
        related_name="second_interviewer_user",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="Interviewer",
    )
    second_remark = models.CharField(
        max_length=135, blank=True, verbose_name="2nd Remarks"
    )

    # HR终面
    hr_score = models.CharField(
        max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name="HR Score"
    )
    hr_responsibility = models.CharField(
        max_length=10,
        choices=HR_SCORE_TYPE,
        blank=True,
        verbose_name="HR Responsibility",
    )
    hr_communication_ability = models.CharField(
        max_length=10,
        choices=HR_SCORE_TYPE,
        blank=True,
        verbose_name="HR Communication",
    )
    hr_logic_ability = models.CharField(
        max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name="HR Logic"
    )
    hr_potential = models.CharField(
        max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name="HR Potential"
    )
    hr_stability = models.CharField(
        max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name="HR Stability"
    )
    hr_advantage = models.TextField(
        max_length=1024, blank=True, verbose_name="Advantages"
    )
    hr_disadvantage = models.TextField(
        max_length=1024, blank=True, verbose_name="Concerns"
    )
    hr_result = models.CharField(
        max_length=256,
        choices=INTERVIEW_RESULT_TYPE,
        blank=True,
        verbose_name="HR Results",
    )
    hr_interviewer_user = models.ForeignKey(
        User,
        related_name="hr_interviewer_user",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="HR Interviewer",
    )
    hr_remark = models.CharField(max_length=256, blank=True, verbose_name="HR Remarks")

    creator = models.CharField(max_length=256, blank=True, verbose_name="Creator")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created Time")
    modified_date = models.DateTimeField(
        auto_now=True, null=True, blank=True, verbose_name="Updated Time"
    )
    last_editor = models.CharField(
        max_length=256, blank=True, verbose_name="Last Editor"
    )

    class Meta:
        db_table = "candidate"
        verbose_name = "Interviewee"
        verbose_name_plural = "Interviewees"

        permissions = [
            ("export", "Can export candidate list"),
            ("notify", "notify interviewer for candidate review"),
        ]

    def __str__(self):
        return self.username
