library(shiny)

diabetesRisk <- function(glucose) glucose/200
#include source statement if function is long?

shinyServer(
        function(input,output) {

                output$inputValue <- renderPrint({input$sizeFamily})
                output$prediction <- renderPrint('Heehee')
                #output$oid2 <- renderPrint({input$id2})
                #output$odate <- renderPrint({input$date})
        }
)