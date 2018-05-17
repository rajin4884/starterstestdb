from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.core.urlresolvers import reverse
from photo.fields import ThumbnailImageField
from django.contrib.auth.models import User
from tagging.fields import TagField
from django.utils import timezone
import datetime

# Create your models here.

@python_2_unicode_compatible
class Album(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField('One Line Description', max_length=100, blank=True)
    owner = models.ForeignKey(User, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('photo:album_detail', args=(self.id,))

@python_2_unicode_compatible
class Photo(models.Model):
    album = models.ForeignKey(Album)
    title = models.CharField(max_length=50)
    image = ThumbnailImageField(upload_to='photo/%Y/%m')
    description = models.TextField('Photo Description', blank=True)
    upload_date = models.DateTimeField('Upload Date', auto_now_add=True)
    owner = models.ForeignKey(User, null=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=(self.id,))


@python_2_unicode_compatible
class Company_info(models.Model):
    company_num = models.ForeignKey('Member_info', on_delete=models.CASCADE)
    company_name = models.CharField(max_length=20, blank = False)
    company_scale = models.CharField( max_length=20, blank = False)
    jobcode = models.ForeignKey('Occupation_type',  on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.id, self.company_name)


class Company_select(models.Model):
    comp_selnum  = models.IntegerField(primary_key=True)
    mem_num = models.ForeignKey('Member_info', on_delete=models.CASCADE)
    company_num = models.ForeignKey('Company_info', on_delete=models.CASCADE)


class Interview_apply(models.Model):
    inter_apply_num = models.IntegerField(primary_key=True)
    comp_selnum = models.ForeignKey('Company_select', on_delete=models.CASCADE)
    interv_snum = models.ForeignKey('Interview_state', on_delete=models.CASCADE, null = True)
    emplo_fnum  = models.ForeignKey('Employee_form', on_delete=models.CASCADE)
    work = models.CharField(max_length=50, blank = False)

    def __str__(self):
        return self.work


class Interview_state(models.Model):
    interv_snum = models.IntegerField(primary_key=True)
    intervs_info = models.CharField(max_length=50, blank = False)

    def __str__(self):
        return self.intervs_info


class Employee_form(models.Model):
    emplo_fnum = models.IntegerField(primary_key=True)
    emplof_info = models.CharField(max_length=50, blank = False)

    def __str__(self):
        return self.emplof_info



### 현진
class Member_info(models.Model):
    mem_num = models.IntegerField(primary_key=True)
    mem_id = models.CharField(max_length=20, blank=False)
    mem_pw = models.CharField(max_length=20, blank=False)
    mem_gender = models.CharField(max_length=2, blank=False)
    mem_birth = models.CharField(max_length=10, blank=False)
    mem_hp = models.CharField(max_length=20)
    mem_email = models.CharField(max_length=50, blank=False)
    mem_add = models.CharField(max_length=200, blank=False)
    mem_name = models.CharField(max_length=20, blank=False)
    mem_rank = models.CharField(max_length=10)
    mem_div = models.CharField(max_length=10)

    def __str__(self):
        return self.mem_name


class Self_introduction(models.Model):
    mem_num = models.ForeignKey('Member_info', on_delete=models.CASCADE)
    self_intro_cont = models.CharField(max_length=2000, blank=False)
    portfolio_file = models.FileField()
    inter_occupation1 = models.ForeignKey('Occupation_type',  on_delete=models.CASCADE)
    inter_occupation2 = models.ForeignKey('Occupation_type', related_name='inter_occupation1', null = True, on_delete=models.CASCADE)
    inter_occupation3 = models.ForeignKey('Occupation_type', related_name='inter_occupation2', null = True, on_delete=models.CASCADE)

    def __str__(self):
        return self.self_intro_cont

class Mento_info(models.Model):
    mem_num = models.ForeignKey('Member_info', on_delete=models.CASCADE)
    profile_pic = models.ImageField(blank=False)
    mento_career = models.CharField(max_length=3, blank=False)
    mento_proof_doc = models.FileField(blank=False)

class Occupation_type(models.Model):
    occ_num = models.IntegerField(primary_key=True)
    occ_name = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.occ_name

class Member_occupation(models.Model):
    mem_occ_num = models.IntegerField(primary_key=True)
    mem_num = models.ForeignKey('Member_info', on_delete=models.CASCADE)
    occ_num = models.ForeignKey('Occupation_type', on_delete=models.CASCADE)



# 혜진

# 게시판 분류
class Board_C(models.Model):
    b_categ_num = models.IntegerField(primary_key=True)
    # board_c = models.ForeignKey('Board')
    b_categ_name = models.CharField(max_length = 20, blank = False)

    def __str__(self):
        return self.b_categ_name

# # 게시판1
# class Board(models.Model):
#     # b_num = models.IntegerField(primary_key=True)
#     # board_c = models.ForeignKey('Board_C', null = True)
#     board_c = models.ForeignKey('Board_C', null = True)
#     # b_categ_num = models.IntegerField(null=True, blank = True) # 삭제(0516)
#     owner = models.ForeignKey(User, null=True)
#     b_title = models.CharField(max_length = 20, blank = False)
#     b_contnet = models.CharField(max_length=500,blank = False)
#     b_published_date = models.DateTimeField(blank=True, null=True)
#     b_hit = models.IntegerField( default = 0)
#     tag = TagField()
#     # b_parent_id = models.IntegerField(null=True, blank = True)
#     # b_parent_id = models.IntegerField(null = True, blank = True)
#
#     def __str__(self):
#         return self.b_title

# 게시판 2
class Board(models.Model):
    board_c = models.ForeignKey('Board_C', null = True)
    b_auth = models.ForeignKey('Member_info', null = True)
    owner = models.ForeignKey(User, null=True)
    b_title = models.CharField(max_length = 20, blank = False)
    b_contnet = models.CharField(max_length=500,blank = False)
    b_password = models.CharField(max_length=30,null = True, blank = True)
    b_published_date = models.DateTimeField(blank=True, null=True)
    b_hit = models.IntegerField( default = 0) # 조회수
    b_ref = models.IntegerField()
    b_re_step = models.IntegerField()
    b_re_level = models.IntegerField()
    tag = TagField()


    def __str__(self):
        return self.b_title

# 후기 게시판
class Review(models.Model):
    mrapply_num = models.ForeignKey('Mrapply', null = True) # 고친버전
    # mrapply_num = models.ForeignKey('Mrapply', on_delete=models.CASCADE) # 원래버전
    r_num = models.IntegerField(primary_key=True)
    # mrapply_num = models.IntegerField(null = True, blank = True)
    mr_title = models.CharField("멘티이름", max_length = 20, null = True, blank = False)
    mto_name = models.CharField("멘토이름", max_length = 20, null = True, blank = False)
    r_score = models.IntegerField("조회수", null = True, blank = True, default=0) # 조회 수
    r_content = models.CharField("내용", max_length=500, null = True, blank = False)
    r_image = models.ImageField(null = True)
    r_like = models.IntegerField("좋아요 수", null = True, blank = True, default = 0)
    r_date = models.DateTimeField("작성날짜",  null = True, auto_now_add=True)

    def __str__(self):
        return self.mr_title


# # 혜리
# # 멘토링찜하기
# class Mr_Wish(models.Model):
#     mr_wish_num = models.IntegerField(primary_key=True)
#     mem_Num = models.ForeignKey('Member_info', on_delete = models.CASCADE) # FK
#     mtr_num = models.ForeignKey('Mtr_info', on_delete = models.CASCADE) # FK


# # 기업찜하기
# class Biz_Wish(models.Model):
#     # 기업 외래키 설정
#     biz_wish_num = models.IntegerField(primary_key=True)
#     mem_Num = models.ForeignKey('Company_info', on_delete = models.CASCADE) # FK
#     mem_Num = models.ForeignKey('Member_info', on_delete = models.CASCADE) # FK


# # 멘토링신청정보
# class Mrapply(models.Model):
#     mrapply_num = models.IntegerField(primary_key=True)
#     mr_wish_num = models.ForeignKey('Mr_Wish', on_delete = models.CASCADE) # FK
#     mrapply_start = models.DateTimeField(auto_now_add=True)
#     mrapply_con = models.IntegerField(blank = False)
#     mr_pay_method = models.CharField(max_length=10, null=False)
#     mr_credit_com = models.CharField(max_length=10, null=False)
#     mr_credit_num = models.IntegerField(blank = False)
#     mr_apporve_num = models.IntegerField(blank = False)
#     mr_approve_date = models.DateTimeField(auto_now_add=True)
#     mr_depositless_name = models.CharField(max_length=10, null=False)
#     mr_depositless_date = models.DateTimeField(auto_now_add=True)
#     mr_depositless_bank = models.CharField(max_length=10, null=False)
#     mr_deposit_date = models.DateTimeField(auto_now_add=True)
#     mr_payamount =  models.IntegerField(blank = False)

#     def __str__(self):
#         return self.mr_pay_method


# # 멘토링신청정보 상태
# class Mrapply_State(models.Model):
#     mrapply_con = models.IntegerField(primary_key=True)
#     mrapply_name = models.CharField(max_length=10, null=False)


# # 면접수수료결제정보
# class Inter(models.Model):
#     # 면접신청번호 외래키 설정
#     inter_num = models.IntegerField(primary_key=True)
#     inter_apply_num = models.ForeignKey('Interview_apply', on_delete = models.CASCADE) #FK
#     inter_pay_method = models.CharField(max_length=10, null=False)
#     inter_credit_com = models.CharField(max_length=10, null=False)
#     inter_credit_num = models.IntegerField(blank = False)
#     inter_apporve_num = models.IntegerField(blank = False)
#     inter_approve_date = models.DateTimeField(auto_now_add=True)
#     inter_depositless_name = models.CharField(max_length=10, null=False)
#     inter_depositless_date = models.DateTimeField(auto_now_add=True)
#     inter_depositless_bank = models.CharField(max_length=10, null=False)
#     inter_deposit_date = models.DateTimeField(auto_now_add=True)
#     inter_payamount =  models.IntegerField(blank = False)

#     def __str__(self):
#         return self.inter_pay_method

# 혜리
# 멘토링찜하기
class Mr_Wish(models.Model):
    mr_wish_num = models.IntegerField(primary_key=True)
    mem_num = models.ForeignKey('Member_info', on_delete = models.CASCADE) # FK
    mtr_num = models.ForeignKey('Mtr_info', on_delete = models.CASCADE) # FK, 180514 수정


# 기업찜하기(혜영이가 해 놓음)
# class Biz_Wish(models.Model):
    # biz_wish_num = models.IntegerField(primary_key=True)
    # 기업 외래키 설정
    # mem_Num = models.ForeignKey('Company_info', on_delete = models.CASCADE) # FK
    # mem_Num = models.ForeignKey('Member_info', on_delete = models.CASCADE) # FK


# 멘토링신청정보
class Mrapply(models.Model):
    mrapply_num = models.IntegerField(primary_key=True)
    mr_wish_num = models.ForeignKey('Mr_Wish', on_delete = models.CASCADE) # FK
    mrapply_con = models.ForeignKey('State', on_delete=models.CASCADE)
    # mrapply_con = models.IntegerField(blank = False)
    mr_pay_method = models.CharField(max_length=10, null=False)
    mr_credit_com = models.CharField(max_length=10, null=True)
    mr_credit_num = models.IntegerField(null=True)
    # mr_apporve_num = models.IntegerField(null=True)
    mr_approve_date = models.DateTimeField(auto_now_add=True)
    mr_depositless_name = models.CharField(max_length=10, null=True)
    mr_depositless_date = models.DateTimeField(auto_now_add=True)
    mr_depositless_bank = models.CharField(max_length=10, null=True)
    mr_deposit_date = models.DateTimeField(auto_now_add=True)
    mr_payamount =  models.IntegerField(blank = False)

    def __str__(self):
        return self.mr_pay_method


# 멘토링신청정보 상태
# class Mrapply_State(models.Model):
#     mrapply_con = models.IntegerField(primary_key=True)
#     mrapply_name = models.CharField(max_length=10, null=False)


# 면접수수료결제정보
class Inter(models.Model):
    inter_num = models.IntegerField(primary_key=True)
    # 면접신청번호 외래키 설정
    inter_apply_num = models.ForeignKey('Interview_apply', on_delete = models.CASCADE) # FK
    inter_pay_method = models.CharField(max_length=10, null=False)
    inter_credit_com = models.CharField(max_length=10, null=True)
    inter_credit_num = models.IntegerField(null=True)
    # inter_apporve_num = models.IntegerField(null=True)
    inter_approve_date = models.DateTimeField(auto_now_add=True)
    inter_depositless_name = models.CharField(max_length=10, null=True)
    inter_depositless_date = models.DateTimeField(auto_now_add=True)
    inter_depositless_bank = models.CharField(max_length=10, null=True)
    inter_deposit_date = models.DateTimeField(auto_now_add=True)
    inter_payamount =  models.IntegerField(blank = False)

    def __str__(self):
        return self.inter_pay_method


# 지선
class Mtr_info(models.Model):
    mtr_num = models.IntegerField(primary_key=True)
    mem_num = models.ForeignKey('Mento_info', on_delete=models.CASCADE)#멘토정보
    occ_num = models.ForeignKey('Occupation_type', on_delete=models.CASCADE)
    theme =  models.CharField(max_length=100, blank=True, null=True)
    amount = models.IntegerField(blank = False)
    mtr_content =  models.CharField(max_length=500, blank=True, null=True)
    fixed_people = models.IntegerField(blank = False)

    def __str__(self):
        return self.theme

class Mtr_daily_report(models.Model):
    mtr_daily_num = models.IntegerField(primary_key=True)
    mrapply_num = models.ForeignKey('Mrapply', on_delete=models.CASCADE)
    mtr_lesson = models.ForeignKey('State', on_delete=models.CASCADE)
    mtr_date = models.DateField(auto_now_add=True) # 해당 레코드 생성시 현재 시간 자동저장
    mtr_answer = models.CharField(max_length=500, blank=True, null=True)
    mtr_content = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.mtr_content

class State(models.Model):
    state_num = models.IntegerField(primary_key=True)
    state_name = models.CharField(max_length=10, null=False)
