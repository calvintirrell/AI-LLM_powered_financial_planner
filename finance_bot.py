from openai import OpenAI
import pandas as pd
import test_key as tk

# Set your OpenAI API key (you need to get it from OpenAI first)
# Maintain security by importing the API secret key from another file
client = OpenAI(api_key=tk.secret_key)

def finance_planning():
    """
    Provides a detailed financial plan for a client based on their income, expenses, and financial goals.

    This function uses the OpenAI API to generate a personalized financial plan. It takes into account the client's monthly income, 
    expenses, debt, and financial goals, and provides a 7-year plan to maximize investing for retirement and build an emergency fund.

    The function returns a string containing the detailed financial plan, including specific numbers, timelines, and guidance on a 
    monthly and annual basis.
    """
    
    # Call the OpenAI API to analyze the data (model selection, length of response, context and prompt to answer)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        max_tokens=2000,
        messages=[
        {"role": "system", "content": "You are a financial planning and wealth management expert in the personal finance industry. "
                                      "Your detailed knowledge and understanding of this industry, is very important to the success of your clients. "
                                      "You excel at understanding client needs and providing specific numbers, timelines and guidance on a monthly and annual basis for clients. "},
        {"role": "user", "content": f"You are a financial and wealth planning expert. Based on the provided client information and the following details, create a detailed 7-year (84-month) plan to maximize retirement investing, debt repayment, and emergency fund savings:"
                                    f"Retirement Investing: Maximize contributions to a 401(k) and Roth IRA each year."
                                    f"Debt Repayment: The client has $170,000 in student loans at an average interest rate of 6.5%. These loans must be paid off within 6 years, with no more than $2,500 allocated monthly to student loan payments."
                                    f"Emergency Fund: Build an emergency fund within 24 months that covers 12+ months of living expenses (excluding retirement investments and emergency fund contributions)."
                                    f"Monthly living expenses (excluding student loan payments, investments, and emergency fund contributions) are $3,500. After reaching the emergency fund target, reduce contributions towards it by 50%."
                                    f"Income and Allocation: Monthly post-tax income is $8,235. Do not exceed this income when allocating funds. Avoid reducing monthly investment amounts to meet emergency fund goals."
                                    f"Excess Funds: Once the student loans are fully paid off in 6 years, distribute excess funds (after retirement contributions, emergency fund contributions, and living expenses) to high-yield accounts as follows:"
                                    f"First priority: Robinhood Gold account with the highest interest rate. Second priority: Apple Savings account. Do not allocate excess funds to traditional checking or savings accounts."
            }
        ]
    )
    
    # Extract and return the response from OpenAI
    return response.choices[0].message.content


# Main function to demonstrate the use
if __name__ == "__main__":
    analysis = finance_planning()
    print("Analysis Result:")
    print(analysis)
