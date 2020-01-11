import time
from helper import *
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Module():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.authenticate = Authenticate(self.driver)

    # Interaction
    def draggable(self):
        driver = self.driver        
        authenticate(driver)
        time.sleep(3)

        move_to_module_page(driver, "draggable.php")
        
        locator = lambda id : driver.find_element_by_id(id)

        # tab 1
        move_to_next_frame(driver, 0, "#example-1-tab-1")
        drag_and_drop_by_offset(driver, locator("draggable"), 150, 50)
        time.sleep(2)

        # tab 2
        move_to_next_frame(driver, 1, "#example-1-tab-2")
        drag_and_drop_by_offset(driver, locator("draggable"), 0, 50)
        time.sleep(1)
        drag_and_drop_by_offset(driver, locator("draggable2"), 50, 0)
        time.sleep(1)
        drag_and_drop_by_offset(driver, locator("draggable3"), 250, 250)
        time.sleep(1)
        drag_and_drop_by_offset(driver, locator("draggable5"), 50, 50)
        time.sleep(2)

        # tab 3
        move_to_next_frame(driver, 2, "#example-1-tab-3")
        drag_and_drop_by_offset(driver, locator("draggable"), 0, 150)
        time.sleep(1)
        drag_and_drop_by_offset(driver, locator("draggable2"), 150, 0)
        time.sleep(1)
        drag_and_drop_by_offset(driver, locator("draggable3"), 250, 250)
        time.sleep(2)

        # tab 4
        move_to_next_frame(driver, 3, "#example-1-tab-4")
        click_and_hold(driver, locator("draggable"))
        time.sleep(2)
        move_by_offset(driver, 200, 300)
        time.sleep(2)
        release(driver)
        time.sleep(2)

        # tab 5
        move_to_next_frame(driver, 4, "#example-1-tab-5")
        drag_and_drop_by_offset(driver, locator("draggable"), 0, 150)
        time.sleep(2)

    def droppable(self):
        driver = self.driver        
        authenticate(driver)
        time.sleep(3)

        move_to_module_page(driver, "droppable.php")        
        locator = lambda id : driver.find_element_by_id(id)

        # tab 1
        move_to_next_frame(driver, 0, "#example-1-tab-1")
        drag_and_drop(driver, locator("draggable"), locator("droppable"))
        time.sleep(2)

        # tab 2
        move_to_next_frame(driver, 1, "#example-1-tab-2")
        drag_and_drop(driver, locator("draggable"), locator("droppable"))
        time.sleep(1)
        drag_and_drop_by_offset(driver, locator("draggable-nonvalid"), 50, 150)
        time.sleep(2)

        # tab 3
        move_to_next_frame(driver, 2, "#example-1-tab-3")
        drag_and_drop(driver, locator("draggable"), locator("droppable"))
        time.sleep(1)
        drag_and_drop(driver, locator("draggable"), locator("droppable-inner"))
        time.sleep(1)
        drag_and_drop(driver, locator("draggable"), locator("droppable2"))
        time.sleep(1)
        drag_and_drop(driver, locator("draggable"), locator("droppable2-inner"))
        time.sleep(1)

        # tab 4
        move_to_next_frame(driver, 3, "#example-1-tab-4")
        drag_and_drop(driver, locator("draggable"), locator("droppable"))
        time.sleep(1)
        drag_and_drop(driver, locator("draggable2"), locator("droppable"))
        time.sleep(2)

    def resizable(self):
        
        driver = self.driver        
        authenticate(driver)
        time.sleep(3)
        
        move_to_module_page(driver, "resizable.php")
        

        handle ="#resizable > div.ui-resizable-handle:nth-child(4)"
        sideBar ="#resizable > div.ui-resizable-handle.ui-resizable-e"
        bottomBar="#resizable > div.ui-resizable-handle.ui-resizable-s"

        # tab 1
        move_to_next_frame(driver, 0, "#example-1-tab-1")
        element = driver.find_element_by_css_selector(sideBar)
        drag_and_drop_by_offset(driver,element,100,100)
        time.sleep(3)
        element = driver.find_element_by_css_selector(bottomBar)
        drag_and_drop_by_offset(driver,element,100,100)
        time.sleep(3)
        element = driver.find_element_by_css_selector(handle)
        drag_and_drop_by_offset(driver,element,100,100)
        time.sleep(4)
        element = driver.find_element_by_css_selector(handle)
        drag_and_drop_by_offset(driver, element, -250, -250)
        time.sleep(4)

        # tab 2
        move_to_next_frame(driver, 1, "#example-1-tab-2")
        element = driver.find_element_by_css_selector(sideBar)
        drag_and_drop_by_offset(driver,element,100,100)
        time.sleep(3)
        element = driver.find_element_by_css_selector(bottomBar)
        drag_and_drop_by_offset(driver,element,100,100)
        time.sleep(3)
        element = driver.find_element_by_css_selector(handle)
        drag_and_drop_by_offset(driver,element,100,100)
        time.sleep(4)
        element = driver.find_element_by_css_selector(handle)
        drag_and_drop_by_offset(driver, element, -250, -250)
        time.sleep(4)

        # tab 3
        move_to_next_frame(driver, 2, "#example-1-tab-3")
        element = driver.find_element_by_css_selector(sideBar)
        drag_and_drop_by_offset(driver,element,100,100)
        time.sleep(3)
        element = driver.find_element_by_css_selector(bottomBar)
        drag_and_drop_by_offset(driver,element,100,100)
        time.sleep(3)
        element = driver.find_element_by_css_selector(handle)
        drag_and_drop_by_offset(driver, element, -100, -100)
        time.sleep(4)
        element = driver.find_element_by_css_selector(handle)
        drag_and_drop_by_offset(driver,element,150,150)
        time.sleep(4)
        

        # tab 4
        move_to_next_frame(driver, 3, "#example-1-tab-4")
        element = driver.find_element_by_css_selector(sideBar)
        drag_and_drop_by_offset(driver,element,100,100)
        time.sleep(3)
        element = driver.find_element_by_css_selector(bottomBar)
        drag_and_drop_by_offset(driver,element,100,100)
        time.sleep(3)
        element = driver.find_element_by_css_selector(handle)
        drag_and_drop_by_offset(driver,element,100,100)
        time.sleep(4)
        element = driver.find_element_by_css_selector(handle)
        drag_and_drop_by_offset(driver, element, -150, -150)
        time.sleep(4)

        # tab 5
        move_to_next_frame(driver, 4, "#example-1-tab-5")
        element = driver.find_element_by_css_selector(sideBar)
        drag_and_drop_by_offset(driver,element,100,100)
        time.sleep(3)
        element = driver.find_element_by_css_selector(bottomBar)
        drag_and_drop_by_offset(driver,element,100,100)
        time.sleep(3)
        element = driver.find_element_by_css_selector(handle)
        drag_and_drop_by_offset(driver,element,100,100)
        time.sleep(4)
        element = driver.find_element_by_css_selector(handle)
        drag_and_drop_by_offset(driver, element, -200, -200)
        time.sleep(4)

        
    
    def selectable(self):
        driver = self.driver        
        authenticate(driver)
        time.sleep(3) 

        move_to_module_page(driver, "selectable.php")
        

        #tab 1
        move_to_next_frame(driver, 0, "#example-1-tab-1")
        item1= driver.find_element_by_css_selector("#selectable > li:nth-child(1)")
        item1.click()
        time.sleep(1)
        item2= driver.find_element_by_css_selector("#selectable > li:nth-child(2)")
        item2.click()
        time.sleep(1)
        item3= driver.find_element_by_css_selector("#selectable > li:nth-child(3)")
        item3.click()
        time.sleep(1)
        item4= driver.find_element_by_css_selector("#selectable > li:nth-child(4)")
        item4.click()
        time.sleep(1)
        item5= driver.find_element_by_css_selector("#selectable > li:nth-child(5)")
        item5.click()
        time.sleep(1)
        item6= driver.find_element_by_css_selector("#selectable > li:nth-child(6)")
        item6.click()
        time.sleep(1)
        item7= driver.find_element_by_css_selector("#selectable > li:nth-child(7)")
        item7.click()
        time.sleep(1)

        # #tab 2
        # move_to_next_frame(driver, 0, "#example-1-tab-2")
        # items= driver.find_elements_by_css_selector("#selectable")
        # items[0].click
        # time.sleep(3)
        # items[1].click()
        # time.sleep(3)
        # items[2].click()
        # time.sleep(3)
        # items[3].click()
        # time.sleep(3)
        # items[4].click()
        # time.sleep(3)
        # items[5].click()
        # time.sleep(3)
        # items[6].click()
        # time.sleep(3)

        
        # #tab 3
        # move_to_next_frame(driver, 0, "#example-1-tab-3")
        # item1= driver.find_element_by_css_selector("//*[@id="'selectable'"]/li[1]")
        # item1.click()
        # time.sleep(3)
        # item2= driver.find_element_by_css_selector("//*[@id="'selectable'"]/li[2]")
        # item2.click()
        # time.sleep(3)
        # item3= driver.find_element_by_css_selector("//*[@id="'selectable'"]/li[3]")
        # item3.click()
        # time.sleep(3)
        # item4= driver.find_element_by_css_selector("//*[@id="'selectable'"]/li[4]")
        # item4.click()
        # time.sleep(3)
        # item5= driver.find_element_by_css_selector("//*[@id="'selectable'"]/li[5]")
        # item5.click()
        # time.sleep(3)
        # item6= driver.find_element_by_css_selector("//*[@id="'selectable'"]/li[6]")
        # item6.click()
        # time.sleep(3)

    def sortable(self):
        #TODO: Implement tests for the sortable module
        driver = self.driver        
        authenticate(driver)
        time.sleep(3) 

    # Widget
    def accordion(self):
        #TODO: Implement tests for the accordion module
        driver = self.driver        
        authenticate(driver)
        time.sleep(3)

        move_to_module_page(driver, "accordion.php") 

        #tab 1
        move_to_next_frame(driver, 0, "#example-1-tab-1")
        accord2= driver.find_element_by_css_selector("#ui-id-3")
        accord2.click()
        time.sleep(3)
        accord3= driver.find_element_by_css_selector("#ui-id-5")
        accord3.click()
        time.sleep(3)
        accord4= driver.find_element_by_css_selector("#ui-id-7")
        accord4.click()
        time.sleep(3)

        #tab 2
        # move_to_next_frame(driver, 0, "#example-1-tab-2")
        # accord2= driver.find_element_by_css_selector("#ui-id-3")
        # accord2.click()
        # time.sleep(2)
        # accord3= driver.find_element_by_css_selector("#ui-id-5")
        # accord3.click()
        # time.sleep(2)
        # accord4= driver.find_element_by_css_selector("#ui-id-7")
        # accord4.click()
        # time.sleep(2)
        # toggle = driver.find_element_by_css_selector("#toggle")
        # toggle.click()
        # time.sleep(1)
        # accord1= driver.find_element_by_css_selector("#ui-id-1")
        # accord1.click()
        # time.sleep(2)
        # accord2= driver.find_element_by_css_selector("#ui-id-3")
        # accord2.click()
        # time.sleep(2)
        # accord3= driver.find_element_by_css_selector("#ui-id-5")
        # accord3.click()
        # time.sleep(2)

        #tab 3
        # move_to_next_frame(driver, 0, "#example-1-tab-3")
        # accord2= driver.find_element_by_css_selector("#ui-id-3")
        # accord2.click()
        # time.sleep(2)
        # accord3= driver.find_element_by_css_selector("#ui-id-5")
        # accord3.click()
        # time.sleep(2)
        # accord4= driver.find_element_by_css_selector("#ui-id-7")
        # accord4.click()
        # time.sleep(2)

    def autocomplete(self):
        driver = self.driver        
        authenticate(driver)
        time.sleep(3) 

        move_to_module_page(driver, "autocomplete.php")
        
        
        #tab 1
        move_to_next_frame(driver, 0, "#example-1-tab-1")
        elem = driver.find_element_by_css_selector("#tags")
        elem.send_keys("C+")
        time.sleep(3) 
        auto_complete = driver.find_elements_by_css_selector("#ui-id-1")
        auto_complete[0].click()
        time.sleep(3)
        elem.clear()
        elem.send_keys("Ja")
        time.sleep(3) 
        auto_complete3 = driver.find_elements_by_css_selector("#ui-id-1")
        auto_complete3[0].click()
        time.sleep(3)
        elem.clear()
        elem.send_keys("JavaSc")
        time.sleep(3) 
        auto_complete2 = driver.find_elements_by_css_selector("#ui-id-1")
        auto_complete2[0].click()
        time.sleep(3)

        # #tab 2
        # move_to_next_frame(driver, 0, "#example-1-tab-2")
        # elem = driver.find_element_by_css_selector("#tags")
        # elem.send_keys("Ap")
        # time.sleep(3) 
        # auto_complete = driver.find_elements_by_css_selector("#ui-id-1")
        # auto_complete[0].click()
        # time.sleep(3)
        # elem.clear()
        # elem.send_keys("Ba")
        # time.sleep(3) 
        # auto_complete3 = driver.find_elements_by_css_selector("#ui-id-1")
        # auto_complete3[0].click()
        # time.sleep(3)
        # elem.clear()
        # elem.send_keys("For")
        # time.sleep(3) 
        # auto_complete2 = driver.find_elements_by_css_selector("#ui-id-1")
        # auto_complete2[0].click()
        # time.sleep(3)

        # #tab 3
        # move_to_next_frame(driver, 0, "#example-1-tab-3")
        # elem1 = driver.find_element_by_tag_name("input")
        # elem1.clear()
        # elem1.send_keys("ant")
        # time.sleep(3) 
        # auto_complete = driver.find_elements_by_css_selector("#ui-id-1")
        # auto_complete[0].click()
        # time.sleep(3)
        # elem1.clear()
        # elem1.send_keys("annh")
        # time.sleep(3) 
        # auto_complete3 = driver.find_elements_by_css_selector("#ui-id-1")
        # auto_complete3[0].click()
        # time.sleep(3)
        # elem1.clear()
        # elem1.send_keys("andre")
        # time.sleep(2)
        # auto_complete2 = driver.find_elements_by_css_selector("#ui-id-1")
        # auto_complete2[0].click() 
        # elem1.send_keys(" ")
        # time.sleep(1)
        # elem1.send_keys("jo")
        # time.sleep(2) 
        # auto_complete4 = driver.find_elements_by_css_selector("#ui-id-1")
        # auto_complete4[0].click()
        # time.sleep(3)

        


    def datepicker(self):
        #TODO: Implement tests for the datepicker module
        driver = self.driver        
        authenticate(driver)
        time.sleep(3) 

    def menu(self):
        #TODO: Implement tests for the menu module
        driver = self.driver        
        authenticate(driver)
        time.sleep(3) 

    def slider(self):
        #TODO: Implement tests for the slider module
        driver = self.driver        
        authenticate(driver)
        time.sleep(3) 

    def tabs(self):
        #TODO: Implement tests for the tabs module
        driver = self.driver        
        authenticate(driver)
        time.sleep(3) 

    def tooltip(self):
        #TODO: Implement tests for the tooltip module
        driver = self.driver        
        authenticate(driver)
        time.sleep(3)

    # Frames and Windows
    def frames_and_windows(self):
        #TODO: Implement tests for the frames and windows module
        driver = self.driver        
        authenticate(driver)
        time.sleep(3)

    # Dynamic element
    def submit_button_clicked(self):
        #TODO: Implement tests for the submit button clicked module
        driver = self.driver        
        authenticate(driver)
        time.sleep(3)

    def dropdown(self):
        #TODO: Implement tests for the dropdown module
        driver = self.driver        
        authenticate(driver)
        time.sleep(3)

    # Registration
    def registration(self):
        #TODO: Implement tests for the registration module
        driver = self.driver        
        authenticate(driver)
        time.sleep(3)

    # Alert
    def alert(self):
        #TODO: Implement tests for the alert module
        driver = self.driver        
        authenticate(driver)
        time.sleep(3)
 