import os, sys, warnings
import time
from pathlib import Path
warnings.filterwarnings('ignore')
#sys.path.insert(0, os.path.abspath(os.path.join(Path.home(), "rpa_libs")))

from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys

# Nossas libs
#import app
#from plugins.selenium.selenium import Selenium


# In[51]:


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service 


# In[52]:


# Inicializa o driver do navegador (Chrome no exemplo)
#driver = webdriver.Chrome(executable_path='/caminho/para/chromedriver')
driver_path = ChromeDriverManager().install()


# In[53]:


print(driver_path)


# In[59]:


#driver = webdriver.Chrome(ChromeDriverManager().install()) erro
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Correct initialization of Chrome WebDriver using Service
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


# In[62]:


driver.get('https://www.fitenergia.com.br/')


# In[ ]:


driver.find_element(By.XPATH, '/html/body/header/section/div[2]/div[2]/div/div/a').click()


# In[ ]:


driver.find_element(By.XPATH, '//*[@id="user_email"]').send_keys('teste@teste.com'+ Keys.ENTER)


# In[ ]:


driver.find_element(By.XPATH, '//*[@id="user_password"]').send_keys('Password123'+ Keys.ENTER)

time.sleep(30)

