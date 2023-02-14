function telephoneValidator(str) {   
  // The format is 1(570)778-1016 with optional characters of, leading 1, (), -, a single space.
  const telephoneRegex = /^(1\s?)?(\(\d{3}\)|\d{3})[\s\-]?\d{3}[\s\-]?\d{4}$/;   
  
  return telephoneRegex.test(str);
}

console.log(telephoneValidator("1 (555) 555-5555"));
 
