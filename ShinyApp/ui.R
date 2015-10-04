library(shiny)
shinyUI(pageWithSidebar( #gives page format as page with sidebar
                
                ####################################
                      ### Application title ###
                ####################################
                headerPanel("What's for Dinner?"),
                
                
                
                
                ################################
                     ### Side Bar Panel ###
                ################################
                sidebarPanel( 
                        
                        numericInput('sizeFamily', 'Family Size', 1),

                        numericInput('budget','Food Budget ($/wk)',10),
                        submitButton('Enter')
                        ),
                        
                
                ##########################
                    ### Main Panel ###
                ##########################
                mainPanel( 
                        #h3('Main Panel text'),
                        #code('some code'),
                        h3('An app to help you eat healthy while on a budget.'),
                        
                        h3("Recommended Meal Plan"),
                        h4("You entered..."),
                        verbatimTextOutput("inputValue"),
                        h4("Which resulted in a prediction of "),
                        verbatimTextOutput("prediction")

#                         h4('You Entered...'),
#                         verbatimTextOutput("oid2"),
#                         h4('You Entered...'),
#                         verbatimTextOutput("odate")
                        
                )                
                                
                )
                
                
                
        )