#!/usr/bin/env python
import os
import random
import pandas as pd
import numpy as np
from psychopy import visual, core, event, gui
import PIL

# ----------------------
# 1. Setup & Parameters
# ----------------------
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

TIME_LIMIT = 8 
WINDOW_SIZE = [1440, 900] 
BACKGROUND_COLOR = "#1C1C1C"
TEXT_COLOR = "#D5D5D5"
FONT = 'Arial'
TEXT_SIZE = 30
SLIDER_WIDTH = 600
MIN_VAL = 0   # <--- Updated to 0
MAX_VAL = 7 

# ----------------------
# 2. Helper Functions (Exp 1 Logic)
# ----------------------
def normalize_mouse_loc(mouse_x):
    """Converts pixel position to 0-7 scale with 0.1 increments."""
    # Map pixel range [-WIDTH/2, WIDTH/2] to [0, 7]
    norm_loc = (mouse_x + SLIDER_WIDTH / 2) / SLIDER_WIDTH * (MAX_VAL - MIN_VAL) + MIN_VAL
    # Round to nearest 0.1
    norm_loc = round(norm_loc, 1)
    # Bound the value strictly between 0 and 7
    return min(max(norm_loc, float(MIN_VAL)), float(MAX_VAL))

def reverse_normalize_mouse_loc(norm_loc):
    """Converts 0-7 scale back to pixels for the marker."""
    return (norm_loc - MIN_VAL) / (MAX_VAL - MIN_VAL) * SLIDER_WIDTH - SLIDER_WIDTH / 2

def shuffle_no_repeats(trial_list):
    temp_list = list(trial_list)
    random.shuffle(temp_list)
    for i in range(len(temp_list) - 1):
        if temp_list[i]['product_id'] == temp_list[i+1]['product_id']:
            return shuffle_no_repeats(trial_list)
    return temp_list

def create_product_object(win_obj, image_path):
    img_stim = visual.ImageStim(win_obj, pos=(0, 120))
    try:
        img = PIL.Image.open(image_path)
        w, h = img.size
        ratio = max(w / 450, h / 450)
        img_stim.setImage(image_path)
        img_stim.setSize((int(w/ratio), int(h/ratio)))
    except Exception as e:  # CHANGED
        print(f"Error loading: {image_path}")  # CHANGED
        print(f"Reason: {e}")  # CHANGED
    return img_stim

# ----------------------
# 3. Initialization
# ----------------------
dlg = gui.Dlg(title="Participant Info")
dlg.addField('ID:'); dlg.addField('Age:'); dlg.show()
if not dlg.OK: core.quit()

win = visual.Window(size=WINDOW_SIZE, color=BACKGROUND_COLOR, units='pix', fullscr=True)
mouse = event.Mouse(win=win, visible=True)
timer = core.Clock()

# Load Stimuli
csv_path = os.path.join(_thisDir, 'image_table.csv')
stimuli_df = pd.read_csv(csv_path)
#image_folder = os.path.join(_thisDir, 'taste&health')
# ----------------------
# Flexible memory trigger system
# ----------------------

MEMORY_TRIGGERS = {
    'Tapuchips': 1,   # 1 random memory 
    'Nutella': 1,
    'Cheetos': 1,
    'CocaColaZero':1,
}

base_trials = shuffle_no_repeats(stimuli_df.to_dict('records'))
all_trials = list(base_trials)

# Collect all insertion points first, based only on original stimulus trials
memory_insertions = []

for product_name, n_probes in MEMORY_TRIGGERS.items():
    product_indices = [
        i for i, trial in enumerate(base_trials)
        if trial['product_id'] == product_name
    ]

    if len(product_indices) == 0:
        continue

    chosen_indices = random.sample(
        product_indices,
        min(n_probes, len(product_indices))
    )

    for idx in chosen_indices:
        memory_insertions.append((idx + 1, {
            'trial_type': 'memory', 
            'correct_product': product_name
        }))

# Insert from the end so indices stay correct
for insert_idx, memory_trial in sorted(memory_insertions, key=lambda x: x[0], reverse=True):
    all_trials.insert(insert_idx, memory_trial)

# ----------------------
# 4. Visual Elements
# ----------------------
slider_kwargs = {
    'win': win, 'size': (SLIDER_WIDTH, 30), 'style': 'slider',
    'ticks': [0, 1, 2, 3, 4, 5, 6, 7], # <--- Ticks start at 0
    'labels': ['0', '1', '2', '3', '4', '5', '6', '7'],
    'color': TEXT_COLOR, 'labelColor': TEXT_COLOR, 'markerColor': TEXT_COLOR,'granularity': 0.1
}

questions = {
    'liking': visual.TextStim(win, text='How much do you LIKE the product?', pos=(0, -160), height=TEXT_SIZE, color=TEXT_COLOR,wrapWidth=1000),
    'taste': visual.TextStim(win, text='How TASTY do you think the product is?', pos=(0, -160), height=TEXT_SIZE, color=TEXT_COLOR,wrapWidth=1000),
    'health': visual.TextStim(win, text='How HEALTHY do you think the product is?', pos=(0, -160), height=TEXT_SIZE, color=TEXT_COLOR,wrapWidth=1000)
}

shared_slider = visual.Slider(pos=(0, -250), **slider_kwargs)
left_anchor = visual.TextStim(
    win,
    text='Not at all',
    pos=(-SLIDER_WIDTH/2, -300),
    height=22,
    color=TEXT_COLOR,
    alignText='center',
    anchorHoriz='center'
)

right_anchor = visual.TextStim(
    win,
    text='Very much',
    pos=(SLIDER_WIDTH/2, -300),
    height=22,
    color=TEXT_COLOR,
    alignText='center',
    anchorHoriz='center'
)
timer_text = visual.TextStim(win, text='', pos=(0, -280), height=20, color='white')

# ----------------------
# 5. Trial Logic
# ----------------------
def run_sequential_trial(trial_info):
    full_image_path = os.path.join(_thisDir, str(trial_info['image_path']))  # CHANGED
    print("Loading image:", full_image_path)  # CHANGED
    product_stim = create_product_object(win, full_image_path)  # CHANGED
    
    q_names = ['liking', 'taste', 'health']
    random.shuffle(q_names)
    trial_results = {}

    for q in q_names:
        shared_slider.reset()

        # --- Set random start of slider ---
        rand_x = random.randint(int(-SLIDER_WIDTH/2), int(SLIDER_WIDTH/2))
        mouse.setPos((rand_x, -180))
        core.wait(0.05)
        actual_start_x = mouse.getPos()[0]
        init_slider_val = normalize_mouse_loc(actual_start_x)

        # Reset clocks
        timer.reset()
        rt = None

        while timer.getTime() < TIME_LIMIT:
            product_stim.draw()
            questions[q].draw()
            shared_slider.draw()
            left_anchor.draw()
            right_anchor.draw()

            # Mouse-follow logic
            mouse_x = mouse.getPos()[0]
            current_val = normalize_mouse_loc(mouse_x)
            shared_slider.markerPos = current_val

            # Draw current rating
            choice_stim = visual.TextStim(win, text=f"Rating: {current_val:.1f}",
                                          pos=(0, -200), height=25, color=TEXT_COLOR)
            choice_stim.draw()
            win.flip()
            keys = event.getKeys(modifiers=True)
            for key, mods in keys:
                if key == 'escape' and mods['shift']:
                    core.quit() # This closes the experiment immediately
            # Check for click to confirm
            if mouse.getPressed()[0]:
                trial_results[q] = current_val
                rt = timer.getTime()
                
                # 1. Clear the screen immediately after the click
                win.flip() 
                
                # 2. Apply the delay before the 'for' loop moves to the next 'q'
                core.wait(0.5) # Adjust delay time here (e.g., 0.5 seconds)
                break
        if q not in trial_results:  # This means the loop finished without a click
            warning_msg = visual.TextStim(win, text='Please answer before 8 seconds', 
                                         pos=(0, 0), height=30, color='red')
            warning_msg.draw()
            win.flip()
            core.wait(2.0) # Show the warning for 2 seconds
            
            trial_results[q] = None
            rt = None
        # Fill in values if timed out
        if q not in trial_results:
            trial_results[q] = None
            rt = None

        # Save initial value and RT
        trial_results[f"{q}_initMouse"] = init_slider_val
        trial_results[f"{q}_RT"] = rt

            
    return trial_results
def run_memory_trial(trial_info):

    correct_product = trial_info['correct_product']

    # Get all unique products
    all_products = stimuli_df['product_id'].unique().tolist()

    # Select 2 wrong options
    wrong_options = random.sample(
        [p for p in all_products if p != correct_product],
        2
    )

    options = wrong_options + [correct_product]
    random.shuffle(options)

    question = visual.TextStim(
        win,
        text="Which product was shown in the previous trial?\n\n"
        "Use keys 1, 2, or 3 to respond.",
        pos=(0, 200),
        height=TEXT_SIZE,
        color=TEXT_COLOR
    )

    option_texts = []
    for i, opt in enumerate(options):
        txt = visual.TextStim(
            win,
            text=f"{i+1}. {opt}",
            pos=(0, 100 - i*80),
            height=TEXT_SIZE,
            color=TEXT_COLOR
        )
        option_texts.append(txt)

    selected = None
    timer.reset()

    while selected is None:
        question.draw()
        for txt in option_texts:
            txt.draw()
        win.flip()

        keys = event.waitKeys(keyList=['1','2','3'])
        selected = int(keys[0]) - 1

    chosen_product = options[selected]
    is_correct = chosen_product == correct_product
    rt = timer.getTime()

    return {
        'memory_correct_product': correct_product,
        'memory_chosen': chosen_product,
        'memory_accuracy': is_correct,
        'memory_RT': rt
    }

# --- WELCOME MESSAGE ---
welcome_text = visual.TextStim(
    win,
    text="Welcome!\nThis is a decision-making experiment.\n\nPress SPACE to start.",
    height=TEXT_SIZE,
    wrapWidth=1000,
    color=TEXT_COLOR,
    alignText='center'
)
welcome_text.draw()
win.flip()
event.waitKeys(keyList=['space'])

# --- INSTRUCTIONS SLIDE ---
instructions_text = visual.TextStim(
    win,
    text=(
        "INSTRUCTIONS:\n\n"
        "You will see images of products.\n"
        "Please answer these 3 questions:\n"
        "- How much do you LIKE the product?\n"
        "- How TASTY do you think the product is?\n"
        "- How HEALTHY do you think the product is?\n\n"
        "Rate each question from 0 (not at all) to 7 (very much).\n\n"
        "Use the mouse to move the slider and click to confirm your rating.\n"
        "You will have 8 seconds to answer each question.\n\n"
        "Press SPACE to begin the experiment."
    ),
    height=TEXT_SIZE,
    wrapWidth=1000,
    color=TEXT_COLOR,
    alignText='center'
)
instructions_text.draw()
win.flip()
event.waitKeys(keyList=['space'])
# --- MAIN LOOP ---
results = []
for trial in all_trials:

    # If memory trial
    if trial.get('trial_type') == 'memory':

        memory_data = run_memory_trial(trial)

        trial_data = {
            **trial,
            **memory_data,
            'participant': dlg.data[0],
            'age': dlg.data[1]
        }

        results.append(trial_data)

    else:
        # Fixation
        visual.TextStim(win, text='+', height=50, color=TEXT_COLOR).draw()
        win.flip()
        core.wait(0.5)

        ratings = run_sequential_trial(trial)

        trial_data = {
            **trial,
            **ratings,
            'participant': dlg.data[0],
            'age': dlg.data[1]
        }

        results.append(trial_data)

# --- SAVE RESULTS ---
data_dir = os.path.join(_thisDir, 'data')
os.makedirs(data_dir, exist_ok=True)  # create data folder if missing
save_path = os.path.join(data_dir, f"data_{dlg.data[0]}.csv")

df = pd.DataFrame(results)
df.to_csv(save_path, index=False)
print(f"Results saved to: {save_path}")

# --- END SCREEN ---
end_text = visual.TextStim(win, text="Thank you!\nPress any key to exit.", 
                           height=TEXT_SIZE, color=TEXT_COLOR, alignText='center')
end_text.draw()
win.flip()
event.waitKeys()
win.close()
core.quit()