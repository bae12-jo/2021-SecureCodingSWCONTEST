# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order                                                                                                   
#   * Make sure each model has one field with primary_key=True                                                                  
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior                                   
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table                        
# Feel free to rename the models, but don't rename db_table values or field names.                                              
from django.db import models                                                                                                    
                                                                                                                                
                                                                                                                                
class AuthGroup(models.Model):                                                                                                  
    name = models.CharField(unique=True, max_length=150)                                                                        
                                                                                                                                
    class Meta:                                                                                                                 
        managed = False                                                                                                         
        db_table = 'auth_group'                                                                                                 
                                                                                                                                
                                                                                                                                
class AuthGroupPermissions(models.Model):                                                                                       
    id = models.BigAutoField(primary_key=True)                                                                                  
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)                                                                     
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)                                                         
                                                                                                                                
    class Meta:                                                                                                                 
        managed = False                                                                                                         
        db_table = 'auth_group_permissions'                                                                                     
        unique_together = (('group', 'permission'),)                                                                            
                                                                                                                                
                                                                                                                                
class AuthPermission(models.Model):                                                                                             
    name = models.CharField(max_length=255)                                                                                     
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)                                                    
    codename = models.CharField(max_length=100)                                                                                 
                                                                                                                                
    class Meta:                                                                                                                 
        managed = False                                                                                                         
        db_table = 'auth_permission'                                                                                            
        unique_together = (('content_type', 'codename'),)                                                                       
                                                                                                                                
                                                                                                                                
class AuthUser(models.Model):                                                                                                   
    password = models.CharField(max_length=128)                                                                                 
    last_login = models.DateTimeField(blank=True, null=True)                                                                    
    is_superuser = models.IntegerField()                                                                                        
    username = models.CharField(unique=True, max_length=150)                                                                    
    first_name = models.CharField(max_length=150)                                                                               
    last_name = models.CharField(max_length=150)                                                                                
    email = models.CharField(max_length=254)                                                                                    
    is_staff = models.IntegerField()                                                                                            
    is_active = models.IntegerField()                                                                                           
    date_joined = models.DateTimeField()                                                                                        
                                                                                                                                
    class Meta:                                                                                                                 
        managed = False                                                                                                         
        db_table = 'auth_user'                                                                                                  
                                                                                                                                
                                                                                                                                
class AuthUserGroups(models.Model):                                                                                             
    id = models.BigAutoField(primary_key=True)                                                                                  
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)                                                                       
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)                                                                     
                                                                                                                                
    class Meta:                                                                                                                 
        managed = False                                                                                                         
        db_table = 'auth_user_groups'                                                                                           
        unique_together = (('user', 'group'),)                                                                                  
                                                                                                                                
                                                                                                                                
class AuthUserUserPermissions(models.Model):                                                                                    
    id = models.BigAutoField(primary_key=True)                                                                                  
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)                                                                       
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)                                                           
                                                                                                                                
    class Meta:                                                                                                                 
        managed = False                                                                                                         
        db_table = 'auth_user_user_permissions'                                                                                 
        unique_together = (('user', 'permission'),)                                                                             
                                                                                                                                
                                                                                                                                
class Custom(models.Model):                                                                                                     
    study_index = models.IntegerField(primary_key=True)                                                                         
    study_deposit = models.CharField(max_length=45, blank=True, null=True)                                                      
    study_fine = models.CharField(max_length=45, blank=True, null=True)                                                         
    study_reward = models.CharField(max_length=45, blank=True, null=True)                                                       
    user_index = models.IntegerField(unique=True)                                                                               
    mod_time = models.DateTimeField()                                                                                           
                                                                                                                                
    class Meta:                                                                                                                 
        managed = False                                                                                                         
        db_table = 'custom'                                                                                                     
                                                                                                                                
                                                                                                                                
class DjangoAdminLog(models.Model):                                                                                             
    action_time = models.DateTimeField()                                                                                        
    object_id = models.TextField(blank=True, null=True)                                                                         
    object_repr = models.CharField(max_length=200)                                                                              
    action_flag = models.PositiveSmallIntegerField()                                                                            
    change_message = models.TextField()                                                                                         
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)                             
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)                                                                       
                                                                                                                                
    class Meta:                                                                                                                 
        managed = False                                                                                                         
        db_table = 'django_admin_log'                                                                                           
                                                                                                                                
                                                                                                                                
class DjangoContentType(models.Model):                                                                                          
    app_label = models.CharField(max_length=100)                                                                                
    model = models.CharField(max_length=100)                                                                                    
                                                                                                                                
    class Meta:                                                                                                                 
        managed = False                                                                                                         
        db_table = 'django_content_type'                                                                                        
        unique_together = (('app_label', 'model'),)                                                                             
                                                                                                                                
                                                                                                                                
class DjangoMigrations(models.Model):                                                                                           
    id = models.BigAutoField(primary_key=True)                                                                                  
    app = models.CharField(max_length=255)                                                                                      
    name = models.CharField(max_length=255)                                                                                     
    applied = models.DateTimeField()                                                                                            
                                                                                                                                
    class Meta:                                                                                                                 
        managed = False                                                                                                         
        db_table = 'django_migrations'                                                                                          
                                                                                                                                
                                                                                                                                
class DjangoSession(models.Model):                                                                                              
    session_key = models.CharField(primary_key=True, max_length=40)                                                             
    session_data = models.TextField()                                                                                           
    expire_date = models.DateTimeField()                                                                                        
                                                                                                                                
    class Meta:                                                                                                                 
        managed = False                                                                                                         
        db_table = 'django_session'                                                                                             
                                                                                                                                
                                                                                                                                
class Post(models.Model):                                                                                                       
    post_index = models.IntegerField(primary_key=True)                                                                          
    study_index = models.IntegerField(unique=True)                                                                              
    post_name = models.CharField(max_length=45)                                                                                 
    user_index = models.IntegerField(unique=True)                                                                               
    user_name = models.CharField(max_length=10)                                                                                 
    contents = models.CharField(max_length=5000)                                                                                
    file_index = models.IntegerField(unique=True, blank=True, null=True)                                                        
    comments = models.CharField(max_length=2000, blank=True, null=True)                                                         
                                                                                                                                
    class Meta:                                                                                                                 
        managed = False                                                                                                         
        db_table = 'post'                                                                                                       
                                                                                                                                
                                                                                                                                
class Study(models.Model):                                                                                                      
    study_code = models.CharField(primary_key=True, max_length=20)                                                              
    study_index = models.IntegerField(unique=True)                                                                              
    study_name = models.CharField(max_length=30)                                                                                
    study_pwd = models.PositiveIntegerField(blank=True, null=True)                                                              
    user_index = models.IntegerField(unique=True)                                                                               
    study_admin = models.CharField(max_length=1, blank=True, null=True)                                                         
    user_name = models.CharField(max_length=10)                                                                                 
    study_deposit = models.CharField(max_length=5, blank=True, null=True)                                                       
    study_fine = models.CharField(max_length=5, blank=True, null=True)                                                          
    study_reward = models.CharField(max_length=5, blank=True, null=True)                                                        
    study_rule = models.CharField(max_length=4000)                                                                              
                                                                                                                                
    class Meta:                                                                                                                 
        managed = False                                                                                                         
        db_table = 'study'                                                                                                      
                                                                                                                                
                                                                                                                                
class User(models.Model):                                                                                                       
    user_index = models.IntegerField(primary_key=True)                                                                          
    user_id = models.CharField(unique=True, max_length=10)                                                                      
    user_pwd = models.CharField(max_length=15)                                                                                  
    user_name = models.CharField(max_length=10)                                                                                 
    user_phone = models.CharField(unique=True, max_length=15)                                                                   
    user_email = models.CharField(unique=True, max_length=50)                                                                   
    user_addr = models.CharField(max_length=100)                                                                                
    study_index = models.IntegerField(unique=True, blank=True, null=True)                                                       
    user_account_index = models.IntegerField(unique=True, blank=True, null=True)                                                
    user_balance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)                                  
                                                                                                                                
    class Meta:                                                                                                                 
        managed = False                                                                                                         
        db_table = 'user'                                                                                                       
                                                                                                                                
                                                                                                                                
class Wallet(models.Model):                                                                                                     
    user_account_index = models.IntegerField(primary_key=True)                                                                  
    user_index = models.IntegerField(unique=True)                                                                               
    user_account = models.CharField(unique=True, max_length=20, blank=True, null=True)                                          
    account_name = models.CharField(max_length=20, blank=True, null=True)                                                       
    user_balance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)                                  
                                                                                                                                
    class Meta:                                                                                                                 
        managed = False                                                                                                         
        db_table = 'wallet'                                                                                                     