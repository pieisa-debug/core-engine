// parser.js

import { join } from 'path';

const parser = (input, config) => {
    if (typeof input !== 'string') {
        throw new Error('Input must be a string.');
    }

    if (config === null) {
        throw new Error('Config cannot be null.');
    }

    if (!config.hasOwnProperty('templatePath')) {
        throw new Error('Template path must be defined in the config.');
    }

    const templatePath = join(config.templatePath, input);

    if (!fs.existsSync(templatePath)) {
        throw new Error(`Template not found at ${templatePath}`);
    }

    const templateContent = fs.readFileSync(templatePath, 'utf8');

    const template = Handlebars.compile(templateContent);

    const data = {
        input,
        // Add default data here if needed
    };

    const output = template(data);

    return output;
};

export default parser;